# Swagger Codegen Assignment: Implemented an API to deploy a machine learning model for predicting house prices in Boston
  
## Description

* Pandas (open source, BSD-licensed library providing

* Boston Dataset is a widely used data set in several machine learning projects, below is the description of the dataset.
	Data Set Characteristics:
	* Number of Instances: 506
	* Number of Attributes: 13 numeric/categorical predictive
	* Median Value (attribute 14) is usually the target
	
## Attributes:
- **CRIM** per capita crime rate by town
- **ZN** proportion of residential land zoned for lots over 25,000 sq.ft.
- **INDUS** proportion of non-retail business acres per town
- **CHAS** Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
- **NOX** nitric oxides concentration (parts per 10 million)
- **RM** average number of rooms per dwelling
- **AGE** proportion of owner-occupied units built prior to 1940
- **DIS** weighted distances to five Boston employment centres
- **RAD** index of accessibility to radial highways
- **TAX** full-value property-tax rate per \$10,000
- **PTRATIO** pupil-teacher ratio by town
- **B** 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
- **LSTAT%** lower status of the population
- **MEDV** Median value of owner-occupied homes in \$1000's

Missing Attribute Values: None
Creator: Harrison, D. and Rubinfeld, D.L.

* One endpoint is provided currently for prediction only

  * ```cloudmesh/Boston/predict```
  
## Execution Details without Docker:
* Make sure you have swagger-codegen-cli.jar installed in your working directory
* git clone the swagger directory
* Install below modules
    * `pip install numpy`
    * `pip install pandas`
    * `pip intall scipy`
    * `pip install sklearn`
* On your terminal, using the Makefile provided run the following commands:
  * `make dirs`
  * `make swagger`
  * `make train`
  * `make service`
  * `make start`
  * You should see a message like this:
  ``` 
  Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
  ```
* Test the service using following curl commands in another terminal
    * `curl -X GET http://localhost:8080/cloudmesh/Boston/predict?data=1,2,3,4,5,6,7,8,9,10,11,12,13`
    
* Or using a web browser
	* `http://localhost:8080/cloudmesh/Boston/predict?data=1,2,3,4,5.101,8.09,7,8.0,9,10,11,10,13`
	 
* To kill the service, run:
  * `make stop`
  
* To clean the directories, run:
  * `make clean`
  
## Instructions for docker installation

* git clone the project.

* you need to have docker installed on the machine.

* Build the image from docker file
    * ` make docker-build `

* Start the service using following make command
    * `make docker-start`

* Test the service using following curl commands in another terminal 
  
    * `curl -X GET http://localhost:8080/cloudmesh/Boston/predict?data=1,2,3,4,5,6,7,8,9,10,11,12,13`
* Or using a web browser
	* `http://localhost:8080/cloudmesh/Boston/predict?data=1,2,3,4,5.101,8.09,7,8.0,9,10,11,10,13`
    

* Get the container ID using following command
    * `docker ps`

* Stop the service using following commands
    * `make docker-stop`

* Optional starting mechanism (interactive mode). These need to be used from within a container using command sudo docker exec -it **containerID** bash
  
  * `make start` 
  
  * `make stop`
	
## API informations : 

### End Point : cloudmesh/Boston/predict/

* The endpoint returns all data for categoryname provided 

* Sample curl request
	  
    * `curl -X GET http://localhost:8080/cloudmesh/Boston/predict?data=1,2,3,4,5,6,7,8,9,10,11,12,13`

* Sample json response for GET request
 	
 	`{"houseprice" : 240.00}`