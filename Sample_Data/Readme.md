# Sample_Data 

The **Sample_Data**  directory in the project git repository is the place to store **SAMPLE** datasets which should be of small size (Typically < 5 Mb), **NOT** the entire datasets - if data-sets are large. Since UCI Income data set is small (About 5 Mb training and test combined), we store the full data here for the tutorial. This is rather an exception than convention, since in real client projects the size of data-sets are almost always gonig to be large.

* uci\_income_train.csv: Training data downloaded from http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
* uci\_income_test.csv: Training data downloaded from http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test

Datasets are downloaded using Python code in: Code\01\_Data\_Acquisition\_and\_Understanding. 