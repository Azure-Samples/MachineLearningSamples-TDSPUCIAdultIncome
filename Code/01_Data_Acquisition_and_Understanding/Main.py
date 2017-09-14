#############################################
# Import the necessary modules and libraries
#############################################
from DataPreparation import downloaddata
#############################################
# download data
#############################################
if __name__ == '__main__':

    dest_folder = 'C:\\TempAMLWorkbench\\TDSPUCIAdultIncome'
    trainfilename = 'uci_income_train.csv'
    testfilename = 'uci_income_test.csv'

    downloaddata(dest_folder, trainfilename, testfilename);