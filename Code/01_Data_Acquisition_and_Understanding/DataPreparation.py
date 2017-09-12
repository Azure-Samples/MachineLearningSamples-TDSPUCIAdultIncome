#############################################
# Import the necessary modules and libraries
#############################################
import sys
import csv
import os
import os.path
import io
import pandas as pd
import requests
print(__doc__)

## download data from web to local

def downloaddata(dest_folder, trainfilename, testfilename):
    trainfile = os.path.join(dest_folder,trainfilename)
    testfile = os.path.join(dest_folder,testfilename)
    os.makedirs(os.path.dirname(trainfile), exist_ok=True)
    os.makedirs(os.path.dirname(testfile), exist_ok=True)

    colnames = ['age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country','income']

    train_data_url="http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
    s=requests.get(train_data_url).content
    train_df=pd.read_csv(io.StringIO(s.decode('utf-8')), sep=',', names=colnames, skipinitialspace=True, skip_blank_lines  = True, error_bad_lines = False, skiprows=0, na_values ='NaN').dropna()

    test_data_url="http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test"
    s=requests.get(test_data_url).content
    test_df=pd.read_csv(io.StringIO(s.decode('utf-8')), sep=',', names=colnames, skipinitialspace=True, skip_blank_lines  = True, error_bad_lines = False, skiprows=1, na_values ='NaN').dropna()

    ###########################################################################################
    ## FILTER DATA
    ###########################################################################################
    ## BINARIZE INTO 0/1 LABEL TARGET BASED ON INCOME
    train_df["income"] = train_df["income"].map({ "<=50K": 0, ">50K": 1 })
    test_df["income"] = test_df["income"].map({ "<=50K.": 0, ">50K.": 1 })
    
    train_df.to_csv(trainfile, index=False, encoding='utf-8')
    test_df.to_csv(testfile, index=False, encoding='utf-8')