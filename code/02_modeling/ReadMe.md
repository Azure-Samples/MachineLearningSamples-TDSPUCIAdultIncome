# Code/02_Modeling

We provide a description of each of the files and their function. 

## 1. Feature engineering
### FeatureEngineering.py
    Purpose: engineer features for both training data and test data
    Language: Python
    How it gets used:
    filter_and_transform_TrainData_Features: make features for the trainging data
    filter_and_transform_TestData_Features: make features for the test data
### Main_FeatureEngineering.py
    Purpose: generate features from data and serialize the feature columns to output folder
    Language: Python

## 2. Model creation
### Main_ModelCreation.py
    Purpose: create model based features and write model to output folder
    Language: Python

## 3. Model evaluation
### ScoringAndEvaluation.py
    Purpose: evaluate model
    Language: Python
    How it gets used:
    Get_Class_Probabilities: score data witht a saved model
    Evaluate_Predictions: evaluate performance of a model
### Main_ScoringAndEvaluation.py
    Purpose: evalute model and output the evaluation metrics
    Language: Python
