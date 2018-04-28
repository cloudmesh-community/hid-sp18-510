from pyspark.sql import Row	
from pyspark.sql.functions import *
from pyspark.ml.feature import StandardScaler
from pyspark.ml.linalg import DenseVector
from pyspark.ml.regression import LinearRegression
from pyspark.sql.functions import *
from pyspark.sql.types import *

#Convert the file into Spark data frame
rdd = sc.textFile('/home/hduser/cal_housing.data')
header = sc.textFile('/home/hduser/cal_housing.domain')

rdd = rdd.map(lambda line: line.split(","))

df = rdd.map(lambda line: Row(longitude=line[0], 
                              latitude=line[1], 
                              housingMedianAge=line[2],
                              totalRooms=line[3],
                              totalBedRooms=line[4],
                              population=line[5], 
                              households=line[6],
                              medianIncome=line[7],
                              medianHouseValue=line[8])).toDF()
                              
def convertColumn(df, names, newType):
	for name in names: 
		df = df.withColumn(name, df[name].cast(newType))
	return df 

# Assign all column names to `columns`
columns = ['households', 'housingMedianAge', 'latitude', 'longitude', 'medianHouseValue', 'medianIncome', 'population', 'totalBedRooms', 'totalRooms']

df = convertColumn(df, columns, FloatType())

def transform_data(df):
	df = df.withColumn("medianHouseValue", col("medianHouseValue")/100000)
	roomsPerHousehold = df.select(col("totalRooms")/col("households"))
	populationPerHousehold = df.select(col("population")/col("households"))
	bedroomsPerRoom = df.select(col("totalBedRooms")/col("totalRooms"))
	df = df.withColumn("roomsPerHousehold", col("totalRooms")/col("households")) \
   		   .withColumn("populationPerHousehold", col("population")/col("households")) \
   		   .withColumn("bedroomsPerRoom", col("totalBedRooms")/col("totalRooms"))
   
	df = df.select("medianHouseValue", 
              "totalBedRooms", 
              "population", 
              "households", 
              "medianIncome", 
              "roomsPerHousehold", 
              "populationPerHousehold", 
              "bedroomsPerRoom")
	return df         

df = transform_data(df)	
# Define the `input_data` 
input_data = df.rdd.map(lambda x: (x[0], DenseVector(x[1:])))

# Replace `df` with the new DataFrame
df = spark.createDataFrame(input_data, ["label", "features"])

# Initialize the `standardScaler`
standardScaler = StandardScaler(inputCol="features", outputCol="features_scaled")

# Fit the DataFrame to the scaler
scaler = standardScaler.fit(df)
scaled_df = scaler.transform(df)

# Transform the data in `df` with the scaler
train_data, test_data = scaled_df.randomSplit([.8,.2],seed=1234)

# Initialize `lr`
lr = LinearRegression(labelCol="label", maxIter=100, regParam=0.3, elasticNetParam=0.8)

# Fit the data to the model
linearModel = lr.fit(train_data)

#Lets run this on our test dataset
predicted = linearModel.transform(test_data)

# Extract the predictions and the "known" correct labels
predictions = predicted.select("prediction").rdd.map(lambda x: x[0])
labels = predicted.select("label").rdd.map(lambda x: x[0])	

# Zip `predictions` and `labels` into a list
predictionAndLabel = predictions.zip(labels).collect()

# Print out first 5 instances of `predictionAndLabel` 
predictionAndLabel[:5]	

#This model can then be saved easily
lr.save("/home/hduser/lrm_model.model")

# We can save the model using below command
sameModel = LogisticRegressionModel.load("/home/hduser/lrm_model.model")


linearModel.summary.rootMeanSquaredError
