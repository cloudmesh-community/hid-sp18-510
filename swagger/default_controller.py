import os
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from flask import Flask, jsonify, request
import pickle
 
app = Flask(__name__)
 
def get_prediction(data):
    try:
        test = pd.DataFrame(np.array(data).reshape(1,13))

    except Exception as e:
        raise e
          
    model = 'linear_pred_model.pkl'

    if test.empty:
        return(bad_request())
    else:
        #Load the saved model
        print("Loading the model...")
        loaded_model = None	
        path = os.getcwd()
        path = path + '/model/'
        print (path)

        with open(path + model,'rb') as f:
            loaded_model = pickle.load(f)

        print("The model has been loaded...doing predictions now...")

        predictions = loaded_model.predict(test)
        
        prediction_value = list(pd.Series(np.round(predictions,2)))[0]
        #print prediction_value
        #final_predictions = ["predicted housing price"] + prediction_series

        """We can be as creative in sending the responses.
           But we need to send the response codes as well.
        """
        responses = jsonify({"housing price" : prediction_value})
        responses.status_code = 200

        return responses
        
def predict_get(data):  # noqa: E501
    """cpu_get
    Returns housing price of test data set
    :rtype: CPU
    """
    print (data)
    return get_prediction(data)	