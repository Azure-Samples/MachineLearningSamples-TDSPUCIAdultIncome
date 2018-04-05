import unittest
import pandas as pd
from test_functions import *

class Test_A(unittest.TestCase):

    def checkColumnNames(self):
        assert checkColumnNames(file_name, required_columns) == True

    def checkResponseLevels(self):
        assert checkResponseLevels(file_name, response_column) == True

    def checkResponsePercent(self):
        assert checkResponsePercent(file_name, response_column) == True

    def checkMissingRate(self):
        assert checkMissingRate(file_name, threshold) == True

    def checkPredictionLevels(self):
        assert checkPredictionLevels(score_file_name, model_file_name) == True

    def checkPredictionPercent(self):
        assert checkPredictionPercent(score_file_name, model_file_name) == True

if __name__ == "__main__":
    

    file_name = "train.csv" # adjust path if your code and csv are not in the same directory
    score_file_name = "test.csv"
    model_file_name = "adult_income_model.pkl"
    required_columns = ['age','workclass','fnlwgt','education','education_num','marital_status','occupation',
                    'relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country','income']
    response_column = "income"
    threshold = 0.01
    unittest.main()
