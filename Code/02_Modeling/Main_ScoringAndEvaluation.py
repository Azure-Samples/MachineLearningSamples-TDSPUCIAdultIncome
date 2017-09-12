#####################################################################################################
# IMPORT LIBRARIES;
#####################################################################################################
import pandas, numpy as np, os, sys, pathlib, pickle
from ScoringAndEvaluation import Get_Class_Probabilities, Evaluate_Predictions

#####################################################################################################
# SET FILE LOCATION, LOCATION TO TEST DATA AND MODEL FILE
#####################################################################################################
dirpath = 'C:\\TempAMLWorkbench\\TDSPUCIAdultIncome'


# Transformed test data for scoring
transformed_test_file = dirpath + "\\test_data_engineered.pkl"
inFile = open(transformed_test_file, 'rb')
testDataFrame = pickle.load(inFile)
inFile.close()

## Model files
RandomForest_model_file = dirpath + '\\CVRandomForestModel.pkl'
ElasticNet_model_file = dirpath + '\\CVElasticNetModel.pkl'

## PDF files for output of ROC plots
RandomForestROCplotpath = dirpath + '\\RandomForestROCCurve.pdf'
ElasticNetROCplotpath = dirpath + '\\ElasticNetROCCurve.pdf'


#####################################################################################################
# LOAD TEST DATA
#####################################################################################################
y_test = testDataFrame["income"].values
X_test = testDataFrame.drop("income", axis=1)

#####################################################################################################
# PERFORM SCORING AND EVALUATION
#####################################################################################################
if __name__ == '__main__':
    # RANDOMFOREST MODEL
    y_pred = Get_Class_Probabilities(transformed_test_file, RandomForest_model_file);
    RFAuc = Evaluate_Predictions(y_pred, y_test, RandomForestROCplotpath)
    print ("Random Forest AUC: " + str(round(RFAuc, 3)))

    # ELASTICNET MODEL
    y_pred = Get_Class_Probabilities(transformed_test_file, ElasticNet_model_file);
    EnetAuc = Evaluate_Predictions(y_pred, y_test, ElasticNetROCplotpath)
    print ("ElasticNet AUC: " + str(round(EnetAuc, 3)))
