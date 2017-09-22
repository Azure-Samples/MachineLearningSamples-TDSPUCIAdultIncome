# /code

This directory contains all the source code for the project. There are three subdirectories, adhering to the stages of the TDSP lifecycle.

The code sections are organized below in sequential order in which they are to be run. Before running code, do setup.

## Configuration setup before running code
We connect execution environment to Azure account. Open command line window (CLI) by clicking File menu in the top left corner of AML Workbench and choosing "Open Command Prompt." Then run in CLI

    az login

You get a message

    To sign in, use a web browser to open the page https://aka.ms/devicelogin and enter the code <code> to authenticate.

Go to this web page, enter the code and sign into your Azure account. After this step, run in CLI

    az account list -o table

and find the subscription ID of Azure subscription that has your AML Workbench Workspace account. Finally, run in CLI

    az account set -s <subscription ID>

to complete the connection to your Azure subscription.



## /code/01\_data\_acquisition\_and\_understanding
This folder contains code for data preparation and exploratory analyses. It also contains any necessary settings files needed to run the data exploration code. 

Data exploration is performed using the Python 3 [IDEAR (Interactive Data Exploration and Reporting) utility](https://github.com/Azure/Azure-TDSP-Utilities/tree/master/DataScienceUtilities/DataReport-Utils/Python) published as a part of [TDSP suite of data science tools](https://github.com/Azure/Azure-TDSP-Utilities). This utility helps to generate standardized data exploration reports for data containing numerical and categorical features and target. Details of how the Python 3 IDEAR utility was used is provided below. 

The location of the final data exploration report is [here](https://github.com/Azure/MachineLearningSamples-TDSPUCIAdultIncome/tree/master/Docs/DeliveralbeDocs).


Further details on the code used for data preparation and exploratory analysis is provided in [code/01\_data\_acquisition\_and\_understanding](https://github.com/Azure/MachineLearningSamples-TDSPUCIAdultIncome/tree/master/code/01\_data\_acquisition\_and\_understanding).  


## code/02_modeling
This folder contains code related to modeling, including feature engineering, model creation (using cross-validation and hyper-parameter sweeping), and model evaluation. For illustration, two models were created using Elastic Net and Random Forest. Evaluation on test data indicated AUC of both models were comparable, and were > 0.85. 

Detail about the code used in modeling is provided in [code/02_modeling](https://github.com/Azure/MachineLearningSamples-TDSPUCIAdultIncome/tree/master/code/02_modeling).

## code/03_deployment
This folder contains code related to deployment of the Random Forest model in Azure Container Services. Detail about the code used in deployment is provided in [code/03_deployment](https://github.com/Azure/MachineLearningSamples-TDSPUCIAdultIncome/tree/master/code/03_deployment).

## Execution
### Code run in local compute context
In this example, we execute code in **local compute environment** only. Refer to Azure Machine Learning documents for execution details and further options.

### Installation of required libraries
Before you start executing code, from inside the project, go to file menu and open command prompt. Then install the following libraries:

    pip install ipywidgets==5.2.2
    pip install matplotlib
    pip install scikit-learn
    pip install pandas
    pip install requests
    pip install seaborn
    pip install io
    pip install os
    pip install json
    pip install pickle

### Enable Jupyter nbextension
    jupyter nbextension enable --py --sys-prefix widgetsnbextension

### Running .py files
Executing a Python script in a local Python runtime is easy:

    az ml experiment submit -c local my_script.py

###  Running Ipython notebooks
Ipython notebooks can be run within Azure Machine Learning. Simply double-click on the respective files with extenstion .ipnb. This will open the file, with an option to start the Jypyter Notebook Server. Click on "Start Notebook Server" and run your IPython notebook cell by cell, or all the cells at ones from the Run menu.
