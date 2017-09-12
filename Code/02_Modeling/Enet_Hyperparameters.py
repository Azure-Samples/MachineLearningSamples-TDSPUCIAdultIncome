#####################################################################################################
# IMPORT LIBRARIES;
#####################################################################################################
import pandas, numpy as np, os, sys, pathlib, pickle, site, math, statistics
import matplotlib.pyplot as plt; import matplotlib.mlab as mlab;
from sklearn import ensemble, linear_model, grid_search, cross_validation, preprocessing, metrics, datasets, feature_extraction;
from scipy import stats;
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

from azureml.sdk import data_collector
# initialize the logger
run_logger = data_collector.current_run() 

#####################################################################################################
# MAKE OUTPUR DIRECTORY OUTSIDE OF THE GIT REPO ON LOCAL DRIVE
#####################################################################################################
dirpath = 'C:\\TempVienna\\TDSP_Tutorial'
pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True) 

#####################################################################################################
# LOAD TRAIN AND TEST DATA FILES
#####################################################################################################
train_engineered_file = dirpath + "\\train_data_engineered.pkl"
inFile = open(train_engineered_file, 'rb')
train_df = pickle.load(inFile)
inFile.close()

test_engineered_file = dirpath + "\\test_data_engineered.pkl"
inFile = open(test_engineered_file, 'rb')
test_df = pickle.load(inFile)
inFile.close()

## Training data features and target
y_train = train_df["income"].values
X_train = train_df.drop("income", axis=1)

## Testing data features and target
y_test = test_df["income"].values
X_test = test_df.drop("income", axis=1)


#####################################################################################################
# FIT & EVALUATE ELASTIC NET MODEL WITH GRID SEARCH AND CV
#####################################################################################################
# change regularization rate and you will likely get a different accuracy.
alpha = 0.01
# load regularization rate from argument if present
if len(sys.argv) > 1:
    alpha = float(sys.argv[1])

# log the regularization rate
run_logger.log("Regularization Rate", alpha)
print("Regularization rate is {}".format(alpha))

########### TRAIN ELASTICNET MODEL
# Define elastic net training function
SGDeNetLogistic = linear_model.SGDClassifier(loss='log', penalty='elasticnet', alpha=alpha, l1_ratio=0.15)

# Train model
EnetModel = SGDeNetLogistic.fit(X_train, y_train);

########### Generate & evaluate predictions
y_pred = EnetModel.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred, pos_label=1)
AUC = metrics.auc(fpr, tpr);

# log accuracy
run_logger.log("AUC", AUC)
print ("AUC is {}".format(AUC))


########### PERSIST MODEL
model_file = dirpath + '\\ElasticNetModel_alpha-' + str(alpha) + '.pkl'
inFile = open(model_file, 'wb')
joblib.dump(EnetModel, inFile) 
inFile.close()

