import numpy as np
import pandas as pd
import os
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.cross_validation import KFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.pipeline import make_pipeline

import pickle

boston = load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = boston.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)

pipe = make_pipeline(MinMaxScaler(),
                    LinearRegression())
                    
model_sk = pipe

model_sk.fit(X_train, y_train)

path = os.getcwd()
#path = path 
print (path)

pickle.dump(model_sk, open(path + '/linear_pred_model.pkl', 'wb'))

