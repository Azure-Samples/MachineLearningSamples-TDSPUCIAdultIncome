#####################################################################################################
# IMPORT LIBRARIES
#####################################################################################################
import pickle
from FeatureEngineering import filter_and_transform_TrainData_Features, filter_and_transform_TestData_Features
from azureml.logging import get_azureml_logger

###########################################################################################
## FILTER AND TRANSFORM FEATURES
###########################################################################################
dirpath =  os.environ['AZUREML_NATIVE_SHARE_DIRECTORY']
train_input_file = dirpath + "uci_income_train.csv"
train_engineered_file = dirpath + "train_data_engineered.pkl"

test_input_file = dirpath + "uci_income_test.csv"
test_engineered_file = dirpath + "test_data_engineered.pkl"

if __name__ == '__main__':
    # Transform train file
    trainDataFrame = filter_and_transform_TrainData_Features(train_input_file)
    outFile = open(train_engineered_file, 'wb')
    pickle.dump(trainDataFrame, outFile)
    outFile.close()

    # Transform test file, use training file as reference to fit transformations
    testDataFrame = filter_and_transform_TestData_Features(test_input_file, train_input_file)
    outFile = open(test_engineered_file, 'wb')
    pickle.dump(testDataFrame, outFile)
    outFile.close()
    logger = get_azureml_logger()
    logger.log("amlrealworld.uciincome.featureengineering", "true")
