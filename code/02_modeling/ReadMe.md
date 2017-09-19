# /code/02_modeling

We provide a description of each of the files and their function. 

## 1. Feature engineering
### FeatureEngineering.py
    Purpose: define functions for engineering features for both training data and test data
    Language: Python 3
    How it gets used:
    Function - filter_and_transform_TrainData_Features: make features for the trainging data
    Function - filter_and_transform_TestData_Features: make features for the test data
### Main_FeatureEngineering.py
    Purpose: generate features from data and serialize the feature columns to output folder
    Language: Python
    How it gets used: From Azure Maching Learning Command Line
    >az ml experiment submit -c local Main_FeatureEngineering.py

### Main_FeatureEngineering.ipnb
    Purpose: generate features from data and serialize the feature columns to output folder
    Language: Python
    How it gets used: This is an IPython notebook file. Double-click, start Jupyter NB Server, then execute the file cell-by-cell or run all cells from 'Run' menu
    

## 2. Model creation
### Main_ModelCreation.py
    Purpose: train models based on given target and features and saves model to output folder
    Language: Python 3
    How it gets used: From Azure Maching Learning Command Line
    >az ml experiment submit -c local Main_ModelCreation.py

## 3. Model evaluation
### ScoringAndEvaluation.py
    Purpose: defines functions to evaluate model
    Language: Python 3
    How it gets used: 
    Function - Get_Class_Probabilities: score data witht a saved model
    Function - Evaluate_Predictions: evaluate performance of a model
### Main_ScoringAndEvaluation.py
    Purpose: evalute model and output the evaluation metrics
    Language: Python 3
    How it gets used: From Azure Maching Learning Command Line
    >az ml experiment submit -c local Main_ScoringAndEvaluation.py

### Main_ScoringAndEvaluation.py
    Purpose: evalute model and output the evaluation metrics
    Language: Python 3
    How it gets used: This is an IPython notebook file. Double-click, start Jupyter NB Server, then execute the file cell-by-cell or run all cells from 'Run' menu
