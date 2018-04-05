# /code

This directory contains all the source code for the project. There are three sub-directories, adhering to the stages of the TDSP lifecycle.

## /code/01\_data\_acquisition\_and\_understanding
This folder contains code for data preparation and exploratory analyses. It also contains any necessary settings files needed to run the data exploration code. 

Data exploration is performed using the Python 3 [IDEAR (Interactive Data Exploration and Reporting) utility](https://github.com/Azure/Azure-TDSP-Utilities/tree/master/DataScienceUtilities/DataReport-Utils/Python) published as a part of [TDSP suite of data science tools](https://github.com/Azure/Azure-TDSP-Utilities). This utility helps to generate standardized data exploration reports for data containing numerical and categorical features and target. Details of how the Python 3 IDEAR utility was used is provided below. 

The location of the final data exploration report is [here](https://github.com/Azure/MachineLearningSamples-TDSPUCIAdultIncome/tree/master/Docs/DeliveralbeDocs).


Further details on the code used for data preparation and exploratory analysis is provided in [code/01\_data\_acquisition\_and\_understanding](https://github.com/Azure/MachineLearningSamples-TDSPUCIAdultIncome/tree/master/code/01\_data\_acquisition\_and\_understanding).  


## code/02_modeling
This folder contains code related to modeling, including feature engineering, model creation (using cross-validation and hyper-parameter sweeping), and model evaluation. For illustration, two models were created using Elastic Net and Random Forest. Evaluation on test data indicated AUC of both models were comparable, and were > 0.85. 

Details about the code used in modeling is provided in [code/02_modeling](https://github.com/Azure/MachineLearningSamples-TDSPUCIAdultIncome/tree/master/code/02_modeling).

## code/03_deployment
This folder contains code related to deployment of the Random Forest model in Azure Container Services. Details about the code used in deployment is provided in [code/03_deployment](https://github.com/Azure/MachineLearningSamples-TDSPUCIAdultIncome/tree/master/code/03_deployment).

## code/unit_test
This folder provides some python files for unit testing work.
