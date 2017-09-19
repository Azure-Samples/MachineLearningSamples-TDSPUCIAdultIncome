#################################################################################
# SCORE DATA WITH A SAVED MODEL FILE
#################################################################################
def Get_Class_Probabilities (TransformedTestDatPklFile, modelPkllFile):
    import numpy as np
    import pandas
    import pickle
    from sklearn import ensemble, linear_model, model_selection, preprocessing, metrics
    from scipy import stats;
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.externals import joblib

    # Transform test file, use training file as reference to fit transformation
    with open(TransformedTestDatPklFile, 'rb') as f:
        testDataFrame = pickle.load(f)

    testDataFrame["income"].values
    X_test = testDataFrame.drop("income", axis=1)

    # Open Model File
    with open(modelPkllFile, 'rb') as f:
        Model = joblib.load(f) 
    
    # Predict probabilities
    y_pred = Model.predict_proba(X_test)[:, 1];

    return y_pred;



#################################################################################
# EVALUATE PERFORMANCE OF A MODEL ON A TEST DATA AND SAVE A ROC PLOT WITH AUC
#################################################################################
def Evaluate_Predictions (y_pred, y_actual, ROCFile):
    import numpy as np
    import pandas
    import matplotlib.pyplot as plt; 
    from sklearn import ensemble, linear_model, model_selection, preprocessing, metrics

    fpr, tpr, thresholds = metrics.roc_curve(y_actual, y_pred, pos_label=1)
    Auc=metrics.auc(fpr, tpr);

    plt.clf()
    plt.figure(1)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.plot(fpr, tpr, label='ROC')
    plt.xlabel('False positive rate'); plt.ylabel('True positive rate');
    plt.title("AUC: " + str(round(Auc, 3))); 
    plt.legend(loc='best');

    plt.savefig(ROCFile)

    return Auc;
