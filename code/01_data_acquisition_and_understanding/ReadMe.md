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
    >python Main.py

### IDEAR:
For generating standardized data exploration report, we use the [IDEAR utility in Python 3](https://github.com/Azure/Azure-TDSP-Utilities/tree/master/DataScienceUtilities/DataReport-Utils/Python). Further information on this is available in the IDEAR folder.