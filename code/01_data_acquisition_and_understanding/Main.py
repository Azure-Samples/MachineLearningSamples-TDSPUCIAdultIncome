#############################################
# Import the necessary modules and libraries
#############################################
from DataPreparation import downloaddata
from azureml.logging import get_azureml_logger
#############################################
# download data
#############################################
if __name__ == '__main__':

    dest_folder = os.environ['AZUREML_NATIVE_SHARE_DIRECTORY']
    trainfilename = 'uci_income_train.csv'
    testfilename = 'uci_income_test.csv'

    downloaddata(dest_folder, trainfilename, testfilename);
    logger = get_azureml_logger()
    logger.log("amlrealworld.uciincome.datadownload", "true")
