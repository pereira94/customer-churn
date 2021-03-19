import pandas as pd 
import numpy as np 
from pycaret.classification import *
from pandas_profiling import ProfileReport


data = pd.read_csv('https://inputdatapp.s3-us-west-2.amazonaws.com/WA_Fn-UseC_-Telco-Customer-Churn.csv')

#EDA
pr = ProfileReport(data)
pr.to_file(output_file="pandas_profiling1.html")
pr

#Removing columns
data.drop(['customerID','TotalCharges'], axis=1, inplace=True)

#First experiment and model comparison
exp_clf = setup(data = data, target = 'Churn', session_id=111)
compare_models()

#Second experiment and model comparison
exp_clf2 = setup(data = data, target = 'Churn', session_id=111, feature_interaction=True, feature_selection=True)
compare_models()

#Creating logistic model and evaluating it 
log = create_model('lr')
evaluate_model(log)

#Viewing most important features
plot_model(log, plot='feature')

#Saving model
save_model(log, model_name = 'logistic')

