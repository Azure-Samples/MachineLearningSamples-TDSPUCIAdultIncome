# /code/01\_data\_acquisition\_and\_understanding

For source code files associated with data preparation. Data preparation includes one or more of the following steps (not exhaustive):

- Data ingestion
- Data cleanup
- Data reduction
- Data exploration 
- Data visualization

For further information on data feature and defnintion, you can read this document in TDSP public GitHub repo [(link)](https://github.com/Azure/Azure-TDSP-ProjectTemplate/blob/master/Docs/Data_Report/Data%20Defintion.md). And, for what information may be present in a data summary report, you can read this document [(link)](https://github.com/Azure/Azure-TDSP-ProjectTemplate/blob/master/Docs/Data_Report/DataSummaryReport.md).

## Code file documentation

### DataPreparation.py:
    Purpose: download and prepare data
    Language: Python
    How it gets used: Used in Code\01\_Data\_Acquisition\_and_Understanding\Main.py
    downloaddata: download training and test data from the web to local

### Main.py:
    Purpose: call function in DataPreparation.py to download data
    Language: Python
    How it is used: From Azure Machine Learning command line
    >az ml experiment submit -c local Main.py

### IDEAR:
For generating standardized data exploration report, we use the [IDEAR utility in Python 3](https://github.com/Azure/Azure-TDSP-Utilities/tree/master/DataScienceUtilities/DataReport-Utils/Python). This is an INTERACTIVE Jupyter notebook, where you can explore your data, do plotting of features and target, examind their distribution, clustering and then finally select a set of data summaries and pictures to output to a standardized report.

Further information on this is available in the [IDEAR sub-folder](https://github.com/Azure/MachineLearningSamples-TDSPUCIAdultIncome/tree/debraj/code/01_data_acquisition_and_understanding/IDEAR).

Briefly, you will need to double-click on the IDEAR.ipnb IPython notebook. Then click on "Start Jupyter Notebook Server" at the top, and then run the entire notebook.  Then interactively change certain settings for data exploration or plotting. And, finally output a final report from it. The final report will saved in docs/deliverable_docs folder.