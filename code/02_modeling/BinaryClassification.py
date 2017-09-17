#####################################################################################################
# IMPORT LIBRARIES;
#####################################################################################################
import pandas, numpy as np, os, sys, pickle, site, math, statistics, xgboost;
import matplotlib.pyplot as plt; import matplotlib.mlab as mlab;
from sklearn import ensemble, linear_model, grid_search, cross_validation, preprocessing, metrics, datasets, feature_extraction;
from scipy import stats;
# Print the python version, and library path;
print (site.getsitepackages());
#####################################################################################################
# IMPORT RAW TRAINING DATA FROM CSV; 
#####################################################################################################
trainDataCsv = "C:\\dsvm\\notebooks\\PythonML\\Azure-TDSP-Utilities\\Data\\Common\\UCI_Income\\train";
testDataCsv = "C:\\dsvm\\notebooks\\PythonML\\Azure-TDSP-Utilities\\Data\\Common\\UCI_Income\\test";
names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'];
df_train = pandas.read_csv(trainDataCsv, delimiter = ',', names=names,  header=0, skipinitialspace = True, na_values ='NaN', skip_blank_lines  = True, error_bad_lines = False).dropna();
df_valid = pandas.read_csv(testDataCsv, delimiter = ',', names=names,  header=0, skipinitialspace = True, na_values ='NaN', skip_blank_lines  = True, error_bad_lines = False).dropna();
#df.to_pickle('C:\\dsvm\\notebooks\\PythonML\\Azure-TDSP-Utilities\\Data\\Common\\UCI_Income\\train.pkl');

# Create df with one-hot encoded variables for regression functions
catStringCols = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country'];
numericCols = list(set(list(set(list(df_train.columns.values)) - set(catStringCols))) - set(['income']));
# df_train_dummies = pandas.get_dummies(df_train, columns = catStringCols).dropna(axis=0, how='any', thresh=None, subset=None, inplace=False);

# One-hot encode categorical variables
df_train_encoded = df_train[catStringCols].copy();
df_valid_encoded = df_valid[catStringCols].copy();
df_train_numeric = df_train[numericCols].copy();
df_valid_numeric = df_valid[numericCols].copy();

# Scale numerical values from train and test data
for col in numericCols:
    df_train_numeric[col] = preprocessing.StandardScaler().fit_transform(df_train[col].astype(float).reshape(-1,1))
    df_valid_numeric[col] = preprocessing.StandardScaler().fit(df_train[col].astype(float).reshape(-1,1)).transform(df_valid[col].astype(float).reshape(-1,1))

# Convert string/categorical variables to one-hot encoded numerical variables for logistic regression
for col in catStringCols:
    # Transform training data
    Enc_ohe, Enc_label = preprocessing.OneHotEncoder(), preprocessing.LabelEncoder();
    tmp_encoded_train = Enc_label.fit_transform(df_train[col]).reshape(-1,1)
    DF_dummies = pandas.DataFrame(Enc_ohe.fit_transform(tmp_encoded_train).todense(), columns = Enc_label.classes_)
    df_train_numeric = pandas.concat([df_train_numeric, DF_dummies], axis=1)
    # Transform test data
    Enc_ohe, Enc_label = preprocessing.OneHotEncoder(), preprocessing.LabelEncoder();
    tmp_encoded_test = Enc_label.fit(df_train[col]).transform(df_valid[col]).reshape(-1,1)
    DF_dummies = pandas.DataFrame(Enc_ohe.fit(tmp_encoded_train).transform(tmp_encoded_test).todense(), columns = Enc_label.classes_)
    df_valid_numeric = pandas.concat([df_valid_numeric, DF_dummies], axis=1)   


#####################################################################################################
# MODELING USING SIMPLE LOGISTIC REGRESSION;
#####################################################################################################
# Get X and Y, and create train/test split
Y = df_train.loc[:,'income'].values
X = df_train_numeric.values
features = df_train_numeric.columns.values
test_size = 0.33; seed = 7;
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=test_size, random_state=seed)

# Create model
model = linear_model.LogisticRegression()
model.fit(X_train, Y_train)

# Save the model to disk
os.chdir('C:\\dsvm\\notebooks\\PythonML\\Azure-TDSP-Utilities\\DataScienceUtilities\\Modeling\\BinaryClassification')
filename = 'testmodel.pkl'
pickle.dump(model, open(filename, 'wb'))

# Load the model from disk, and score test data
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)

# Score validation data with loaded model
Y_valid = df_valid.loc[:,'income'].values
X_valid = df_valid_numeric.values
result = loaded_model.score(X_valid, Y_valid)
print(result)


#####################################################################################################
# ELASTIC NET MODEL WITH CROSS VALIDATION OPTIMIZATION OF PARAMETER GRID;
#####################################################################################################
# Set grid for sampling
max_iter_search = n_iter_search = 59;

# Set param grid
alphas = []
for p in np.arange(-6, 4, 1):
    alphas.append(math.pow(2,p))
param_grid = {
    'l1_ratio': [0.99,  0.1 ,  0.25,  0.5 ,  0.75,  0.9 ,  0.01],
    'alpha': alphas
}
grid_lengths = np.asarray([len(v) for v in param_grid.values()])
param_grid_size = 1
for l in grid_lengths:
    param_grid_size = param_grid_size * l
if param_grid_size < max_iter_search:
    n_iter_search = param_grid_size

# Define elastic net training function
SGDeNetLogistic = linear_model.SGDClassifier(loss='log', penalty='elasticnet', alpha=0.0001, l1_ratio=0.15)

# Run randomized search
random_search = grid_search.RandomizedSearchCV(SGDeNetLogistic, param_distributions=param_grid, n_iter=n_iter_search, cv=3)
CVModel_Enet = random_search.fit(X_train, Y_train);
predictions = CVModel.predict(X_test);

# The random forest model by itself
Y_pred = CVModel.predict_proba(X_test)[:, 1]
fpr1, tpr1, _ = metrics.roc_curve(Y_test, Y_pred);
fpr, tpr, thresholds = metrics.roc_curve(Y_test, Y_pred, pos_label=1)
plt.figure(1)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr, label='ROC')
plt.xlabel('False positive rate'); plt.ylabel('True positive rate');
plt.title('ROC curve'); plt.legend(loc='best');
plt.show();
metrics.auc(fpr, tpr);

# the histogram of the data
n, bins, patches = plt.hist(Y_pred, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line to histogram
mu = statistics.mean(Y_pred)
sigma = statistics.stdev(Y_pred)
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Smarts')
plt.ylabel('Probability')
title = "Histogram: Probabilities of predictions. mu=" + str(round(mu, 3)) +", sigma=" + str(round(sigma, 3));
plt.title(title)
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()


#####################################################################################################
# RANDOM FOREST MODEL WITH CROSS VALIDATION OPTIMIZATION OF PARAMETER GRID;
#####################################################################################################
# Set grid for sampling
max_iter_search = n_iter_search = 59;

# Set Random Forest classifier learner
RfClassifier = ensemble.RandomForestClassifier(n_estimators=25, criterion='gini', max_depth=None, min_samples_split=20, min_samples_leaf=10, \
    min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, bootstrap=True, oob_score=False, n_jobs=-1, \
    random_state=1234, verbose=0, warm_start=False, class_weight=None);

# Set param grid
param_grid = {
    'n_estimators': [10, 25, 50],
    'min_samples_split': [10, 20, 30],
    'min_samples_leaf': [2, 5, 10, 20]
}
grid_lengths = np.asarray([len(v) for v in param_grid.values()])
param_grid_size = 1
for l in grid_lengths:
    param_grid_size = param_grid_size * l

if param_grid_size < max_iter_search:
    n_iter_search = param_grid_size

# Run randomized search
random_search = grid_search.RandomizedSearchCV(RfClassifier, param_distributions=param_grid, n_iter=n_iter_search, cv=3)
CVModel_RF = random_search.fit(X_train, Y_train);
predictions = CVModel.predict(X_test);

# The random forest model by itself
Y_pred = CVModel.predict_proba(X_test)[:, 1]
fpr1, tpr1, _ = metrics.roc_curve(Y_test, Y_pred);
fpr, tpr, thresholds = metrics.roc_curve(Y_test, Y_pred, pos_label=1)
plt.figure(1)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr, label='ROC')
plt.xlabel('False positive rate'); plt.ylabel('True positive rate');
plt.title('ROC curve'); plt.legend(loc='best');
plt.show();
metrics.auc(fpr, tpr);

#####################################################################################################
# XGBOOST MODEL WITH CROSS VALIDATION OPTIMIZATION OF PARAMETER GRID;
#####################################################################################################
# Set grid for sampling
max_iter_search = n_iter_search = 59;

# Set Random Forest classifier learner
XGBClassifier = xgboost.XGBClassifier()

# Set param grid
param_grid = {
    'learning_rate': [0.1, 0.5],
    'max_depth': [5, 6, 7, 8],
    'colsample_bytree': [0.75, 1],
    'n_estimators': [10, 25, 50],
    'objective': ['binary:logistic']
}
grid_lengths = np.asarray([len(v) for v in param_grid.values()])
param_grid_size = 1
for l in grid_lengths:
    param_grid_size = param_grid_size * l

if param_grid_size < max_iter_search:
    n_iter_search = param_grid_size

# Run randomized search
random_search = grid_search.RandomizedSearchCV(XGBClassifier, param_distributions=param_grid, n_iter=n_iter_search, cv=3)
CVModel_XGB = random_search.fit(X_train, Y_train);
predictions = CVModel.predict(X_test);

# Train final model with best parameters
BestModelFullData = CVModel.best_estimator_.fit(X, Y, label = df_train.columns.values)

# The XGBoost model by itself
Y_pred = CVModel.predict_proba(X_test)[:, 1]
fpr1, tpr1, _ = metrics.roc_curve(Y_test, Y_pred);
fpr, tpr, thresholds = metrics.roc_curve(Y_test, Y_pred, pos_label=1)
plt.figure(1)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr, label='ROC')
plt.xlabel('False positive rate'); plt.ylabel('True positive rate');
plt.title('ROC curve'); plt.legend(loc='best');
plt.show();
metrics.auc(fpr, tpr);

## Plot variable importance
plt.plot = xgboost.plot_importance(BestModelFullData, ax=None, height=0.2, xlim=None, ylim=None, title='Feature importance', xlabel='F score', \
    ylabel='Features', importance_type='weight', max_num_features=None, grid=True)

plt.style.use('ggplot') 
xgboost.plot_importance(booster = BestModelFullData, ylabel=df_train.columns.values)
plt.show();

 # plot
plt.bar(range(len(BestModelFullData.feature_importances_)), BestModelFullData.feature_importances_)
plt.show()
df = pandas.DataFrame(BestModelFullData.feature_importances_, rows=df_train.columns.values);

df = DataFrame(rand(3,2), columns=['A', 'B'])
ax = df_train_numeric.plot(table=True, kind='bar', title='Feature Importance')
for i, each in enumerate(df_train_numeric.index):
    for col in df_train_numeric.columns:
        y = df_train_numeric.ix[each][col]
        ax.text(i, y, y)


################################################################################################
################################################################################################
## BOX PLOT OF SCORES OF CV FOLDS ACROSS ALGOS
enet_scores = cross_validation.cross_val_score(CVModel_Enet.best_estimator_, X, Y);
rf_scores = cross_validation.cross_val_score(CVModel_RF.best_estimator_, X, Y);
xgb_scores = cross_validation.cross_val_score(CVModel_XGB.best_estimator_, X, Y);
data_to_plot = [enet_scores, rf_scores, xgb_scores]
plt.figure(1, figsize=(8, 5))
plt.boxplot(data_to_plot, labels = ['Enet', 'RF', 'XGB'], color = 'lightgray')
plt.show()

forest = CVModel_RF.best_estimator_.fit(X,Y)
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1][0:20][::-1];
plt.figure(1, figsize=(7, 10))
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), features[indices])
plt.xlabel('Relative Importance')
plt.show()

################################################################################################
## CREATE ONSEMBL MODEL USING 3 ALGOS
################################################################################################
## Create data with prediction probabilities of individual models: TRAINING SET
enetPred = pandas.DataFrame(CVModel_Enet.best_estimator_.predict_proba(X_train)[:, 1])
rfPred = pandas.DataFrame(CVModel_RF.best_estimator_.predict_proba(X_train)[:, 1])
XGBPred = pandas.DataFrame(CVModel_XGB.best_estimator_.predict_proba(X_train)[:, 1])
combinedPred = pandas.concat([enetPred, rfPred, XGBPred], axis = 1);
combinedPred.columns = ['enet', 'rf', 'xgb'];
X_train_comb_pred = combinedPred.values

## Create data with prediction probabilities of individual models: TEST SET
enetPred = pandas.DataFrame(CVModel_Enet.best_estimator_.predict_proba(X_test)[:, 1])
rfPred = pandas.DataFrame(CVModel_RF.best_estimator_.predict_proba(X_test)[:, 1])
XGBPred = pandas.DataFrame(CVModel_XGB.best_estimator_.predict_proba(X_test)[:, 1])
combinedPred = pandas.concat([enetPred, rfPred, XGBPred], axis = 1);
combinedPred.columns = ['enet', 'rf', 'xgb'];
X_test_comb_pred = combinedPred.values

## CREATE FINAL MODEL WITH PROBABIBILITIES OF PREDICTION FROM 3 INDIVIDUAL MODELS
LRF = linear_model.LogisticRegression(penalty='l2', dual=False, tol=0.0000001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='liblinear', max_iter=1000, multi_class='ovr', verbose=0, warm_start=False, n_jobs=1)
finalModel = LRF.fit(X_train_comb_pred, Y_train);

## GET FINAL PREDICTIONS FROM TEST SET
Y_pred = finalModel.predict_proba(X_test_comb_pred)[:, 1];
fpr1, tpr1, _ = metrics.roc_curve(Y_test, Y_pred);
fpr, tpr, thresholds = metrics.roc_curve(Y_test, Y_pred, pos_label=1)
plt.figure(1)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr, label='ROC')
plt.xlabel('False positive rate'); plt.ylabel('True positive rate');
plt.title('ROC curve'); plt.legend(loc='best');
plt.show();
metrics.auc(fpr, tpr);





y = train_df_engineered["income"].values
X = train_df_engineered.drop("income", axis=1)

seed = 98052
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=seed,
)

from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(n_estimators=25)
# fit the RandomForest Model
classifier=classifier.fit(X_train,y_train)

