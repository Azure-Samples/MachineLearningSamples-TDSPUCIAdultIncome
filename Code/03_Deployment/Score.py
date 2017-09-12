from azureml.api.schema.dataTypes import DataTypes
from azureml.api.schema.sampleDefinition import SampleDefinition
from azureml.api.realtime.services import generate_schema
import pandas
import pickle

def init():   
    # read in the model file
    dirpath = 'C:\\TempAMLWorkbench\\TDSPUCIAdultIncome'
    ## Location of Model files 
    RandomForest_model_file = dirpath + '\\CVRandomForestModel.pkl'
    from sklearn.externals import joblib
    global model
    model = joblib.load(RandomForest_model_file)
        
def run(input_df):
    import json
    input = input_df.as_matrix()
    try:
            pred = model.predict(input)
            return json.dumps(str(pred[0]))
    except Exception as e:
        return (str(e))

        

def Score_DataFrame (TransformedDataFrame, modelPkllFile):
    import pandas, numpy as np, os, sys, pathlib, pickle, site, math, statistics
    from sklearn import ensemble, linear_model, model_selection, preprocessing, metrics
    from scipy import stats;
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.externals import joblib

    # Open Model File
    inFile = open(modelPkllFile, 'rb')
    Model = joblib.load(inFile) 
    inFile.close()
    
    # Predict probabilities
    y_pred = Model.predict(TransformedDataFrame)

    return y_pred

####################
#  Main function
####################
if __name__ == '__main__':
    
    init()

    dirpath = 'C:\\TempAMLWorkbench\\TDSPUCIAdultIncome'
    # Location of transformed test data for scoring
    TransformedTestDatPklFile = dirpath + "\\test_data_engineered.pkl"

    # Load data-frame for scoring
    inFile = open(TransformedTestDatPklFile, 'rb')
    TransformedTestDataFrame = pickle.load(inFile)
    inFile.close()
    X_test = TransformedTestDataFrame.drop("income", axis=1)
    # Get predictions
    y_pred = run(X_test)
    
    inputs = {"input_df": SampleDefinition(DataTypes.PANDAS, X_test)}
    # The prepare statement writes the scoring file (main.py) and
    # the schema file (service_schema.json) the the output folder.
    generate_schema(run_func=run, inputs=inputs, filepath = dirpath + '\\service_schema.json')
