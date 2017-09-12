#################################################################################
# SCORE TRANSFORMED DATA WITH A SAVED MODEL FILE
#################################################################################
def Score_DataFrame (TransformedDataFrame, modelPkllFile):
    import pandas, numpy as np, os, sys, pathlib, pickle, site, math, statistics
    from sklearn import ensemble, linear_model, model_selection, preprocessing, metrics
    from scipy import stats;
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.externals import joblib

    # Open Model File
    inFile = open(modelPkllFile, 'rb')
    Model = joblib.load(inFile) 
    inFile.close()
    
    # Predict probabilities
    y_pred = Model.predict(TransformedDataFrame)

    return y_pred