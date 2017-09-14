# Data Science Project Report: Azure ML Workbench Sample with UCI Adult Income Classification Dataset using Team Data Science Project Template

[comment]: # (This document is intended to capture the use case summary for this engagement. An executive summary should contain a brief overview of the project, but not every detail. Only the current summary should be captured here and this should be edited over time to reflect the latest details.)
[comment]: # (Some ideas of what to include in the executive summary are detailed below. Please edit and capture the relevant information within each section)
[comment]: # (To capture more detail in the scoping phase, the optional template Scoping.md may be utilized. If more detail around the data, use case, architecture, or other aspects needs to be captured, additional markdown files can be referenced and placed into the Docs folder)

This file contains information about the project being executed (in this case, the UCI Adult Income sample using Azuer Machine Learning Workbench). Typically It is organized according to the Team Data Science (TDSP) Process [Lifecycle stages](https://github.com/Azure/Microsoft-TDSP/blob/master/Docs/lifecycle-detail.md), with an additional section for architecture and environment. 


## 1. Business Understanding
* NOTE: This is a sample, so scope, plan etc., does not necessarily correspond to an actual data science project addressing a specific business question. In an actual project, the problem definiion, scope, plan, personnel sections are likely to be much more detailed, based on discussions with the client (or business owner), the structure of the data science team etc.

### Problem Definition
The purpuse of this sample is to show how to instantiate and execute a projet using the TDSP structure and templates.

The dataset for this project is from the UCI ML Repository [[link]](https://archive.ics.uci.edu/ml/datasets/adult). It is taken from the 1994 US Census database and contains census and income information for about 50,000 individuals. Based on census features, the machine learning task is to predict if the income of an individual is above $50,000 or not (binary classification).

Further information about the dataset is downlaoded and saved [here](\Docs\CustomerDocs\UCI_Adult_Income_Data_Information.txt). 

### Scope
 * Ths scope of this sample is to create a binary classification machine learning model which address the above rediction problem. 
 * We will execute the project in Azure ML Workbench. We will use the Team Data Science Process template om Azure ML Workbench for this project. 
 * We will operationalize the solution in Azure Container Servides for batch and single-mode scoring.

## Plan
We will follow the stages fo the TDSP lifecycle, and organize documentaion and code according to the stages of the lifecycle. Documentation about the work and findings in each of the lifecycle stages is included below in this document. The code is organized into folders which follow the lifecycle stages. Documentation about the code and its execution is 

### Personnel
The project will be execued by one data scientist and a data engineer. Data engineer serves at the project lead, with appropriate credentials to create necessary Azure resources and Visual Studio Online (VSO) Git repositories.

* NOTE: In a customer project additional personnel, from both from a data science team as well as the clieng organization, may be involved (as outlined in the TDSP documentation [[link]](https://github.com/Azure/Microsoft-TDSP/blob/master/Docs/roles-tasks.md))

### Metrics
Performance of the machine learning models will be evaluated on the test set provided by the UCI data repository [[link]](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/). Accuracy will be measured and reorted using AUC. AUC of > 0.8 will be considered acceptable and suitable for deployment.

## 2. Data Acquisition and Understanding
### Raw Data
For detailed information about the data, please see the [description](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names) in the UCI repository. 

This data was extracted from the census bureau database found at: http://www.census.gov/ftp/pub/DES/www/welcome.html. 

There are a total of 48,842 instances (prior to any filtering), mix of continuous and discrete (train=32561, test=16281)

Probability for the label '>50K'  : 23.93% / 24.78% (without unknowns)

Probability for the label '<=50K' : 76.07% / 75.22% (without unknowns)

TARGET: Income class >50K, <=50K.

FEATURES: Age, work class, education level, education level, race, sex, hours of work per week, etc.

### Data Exploration with IDEAR Utility
Data exploration is performed using the Python 3 [IDEAR (Interactive Data Exploration and Reporting) utility](https://github.com/Azure/Azure-TDSP-Utilities/tree/master/DataScienceUtilities/DataReport-Utils/Python) published as a part of [TDSP suite of data science tools](https://github.com/Azure/Azure-TDSP-Utilities). This utility helps to generate standardized data exporation reports for data containing numerical and categorical features and target. Details of how the Python 3 IDEAR utility was used is provided bleow. 

The location of the final data exploration report is here: (.\Docs\DeliveralbeDocs\IDEAR.html).


## 3. Modeling

### Feature Engineering
**Data cleanup: Removing columns and rows**
Prior to feature engineering, we removed two columns fnlwgt, adn education-num. [fnlwgt](https://web.cs.wpi.edu/~cs4341/C00/Projects/fnlwgt) is a sampling weight assigned to every individual, and education is redundant with education-num. We think it is reasonable to use a numerical assignment for education, with higher numbers for higher education levels.

We removed all rows with unknown ('?') values in any one of the folloiwng columns:
workclass, marital-status, occupation, relationship, race, sex, and native-country. 

In addition, we removed rows where the native-country was not one of the ones from which > 100 individuals were recorded. There were < 10 native-countries from where more than 100 individuals were recorded in the 1994 census. Having very few individuals from a native-country could result in unstable models for individuals those native-countries, and cause issues with differences between the training and test sets.

**One-hot encoding categorical features**

Following categorical features were one-hot encoded using Scikit-learn's [preprocessing.OneHotEncoder()](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) function: 'workclass', marital-status, occupation, relationship, race, sex, native_country. So the same encodings are maintained in test set, when applying transformation to test set, we fit the transformation model on the training set and then transformed the test set. 

**Standardization of numerical features**

Numerical features (other than the ones above) were standardized using Scikit-learn's [preprocessing.StandardScaler()](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) function. When applying transformation to test set, we fit the transformation model on the training set and then transformed the test set.

**Saving processed data sets for modeling input**

Training and test data sets were pickled and saved as .pkl files for input into modeling (training data), and model evaluation or deploymenbt (test data).

### Modeling
We created two models with 3-fold cross-validation: Elastic net and Random forest. We used [59-point sampling](http://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf) for random grid search as a strategy for cross-validation. 

### Model evaluation
Accuracy of the models were measured using AUC on the test data set. AUC of both Elastic net and Random forest models were > 0.85. We save both models in pickled .pkl files, and output the ROC plots for both models. In addition, feature importance for the Random forest model are output in a .csv file and plotted in a pdf (top predictive features only).

## 4. Deployment
AUC of both Elastic net and Random forest models were > 0.85. Therefore, per criteria for the threshold for minimum accuracy required for deployment, both models are suitable for deployment. Deployment is performed using Azure Container Services using Azure ML Workbench command line utilities (CLI).


## Architecture & Environments
#### Development
We use Azure (Windows 2012 Server) Data Science Virtual Machine [(DSVM)](https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-data-science-virtual-machine-overview) for development. Azure Machine Learning Workbench is installed on the DSVM. 

We used the TDSP template in Azure Machine Learning Workbench to create a new project, and all code and decuments were developed in this project. Instructions on how to create a new project in TDSP format is provided [here](https://github.com/amlsamples/tdsp/blob/master/Docs/Using-TDSP-in-Vienna.md).

Code is executed in the AMLW Python 3.5 environment using the Azure Machine Learning Workbench CLI. See Azure Machine Learning Workbench product documentation for information on installation and execution. Details about code and its execution is provided in the respective folders and subfolders under \Code.

Outputs generated from data preparation and modeling stages are stored in: C:\\TempAMLWorkbench\\TDSPUCIAdultIncome folder. 

#### Deployment
For deployment, we copied the following files in the project root directory:
1. Json file for input data format
2. The pickled Random Forest model file (CVRandomForesstModel.pkl) 
3. The scoring script, score.py, from the Code\Deployment folder

We then deployed a web-service on a cluster (see instructions on step 10 [here](https://github.com/Azure/ViennaDocs/blob/master/Documentation/tutorial-classifying-iris.md)). In cluster mode,  service is run in the Azure Container Service (ACS). The operationalization environment provisions Docker and Kubernetes in the cluster to manage the web service deployment.


[comment]: # (If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.)

## Reference Documents
* Version control repository - <Add your own link>
* OneNote or other locations with important documents - <Add your own link>
* [Documents from the Customer or Client](./Docs/CustomerDocs)
* [Customer Deliverables](./Docs/DeliveralbeDocs)