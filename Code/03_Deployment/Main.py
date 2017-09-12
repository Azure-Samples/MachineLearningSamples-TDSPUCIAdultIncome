#####################################################################################################
# IMPORT LIBRARIES;
#####################################################################################################
import pandas, numpy as np, os, sys, pathlib, pickle
from Deployment import Score_DataFrame

#####################################################################################################
# SET FILE LOCATION, LOCATION TO TEST DATA AND MODEL FILE
#####################################################################################################
dirpath = 'C:\\TempAMLWorkbench\\TDSPUCIAdultIncome'

# Location of transformed test data for scoring
TransformedTestDatPklFile = dirpath + "\\test_data_engineered.pkl"

## Location of Model files
RandomForest_model_file = dirpath + '\\CVRandomForestModel.pkl'

#####################################################################################################
# PERFORM SCORING AND EVALUATION
#####################################################################################################
if __name__ == '__main__':
    # Load data-frame for scoring
    inFile = open(TransformedTestDatPklFile, 'rb')
    TransformedTestDataFrame = pickle.load(inFile)
    inFile.close()

    X_test = TransformedTestDataFrame.drop("income", axis=1)
    
    # Get predictions
    y_pred = Score_DataFrame(X_test, RandomForest_model_file)