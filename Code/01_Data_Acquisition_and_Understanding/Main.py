########################################################################################################################
# This program builds regression model for bike forecasting
# Inputs: expects train and test data files with following
#          columns (in order, the names are immaterial)
#         Hour	Weekday	start station id	RideInitiationCount	N_DryBulbTemp	N_RelativeHumidity	N_WindSpeed
# Outputs: pickled/numpy files for regression model and tranforms
#          also prints the R-Sq on Training data and RMSE for test
########################################################################################################################

#############################################
# Import the necessary modules and libraries
#############################################
import sys
import csv
import os
import os.path
print(__doc__)

import sys  
sys.path.append("Code\\01_DataPreparation")  

from DataPreparation import downloaddata

#############################################
# This is the main execution
# we read the train and test files 
# do feature preprocessing
# build model and do xval on train
# do out of sample val on test
#############################################
if __name__ == '__main__':

    dest_folder = 'C:\\TempAMLWorkbench\\TDSPUCIAdultIncome'
    trainfilename = 'uci_income_train.csv'
    testfilename = 'uci_income_test.csv'

    downloaddata(dest_folder, trainfilename, testfilename);