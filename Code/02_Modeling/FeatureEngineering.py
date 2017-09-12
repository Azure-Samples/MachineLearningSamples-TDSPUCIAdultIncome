########################################################################################################
# TRANSFORM TRAINING DATA
########################################################################################################
def filter_and_transform_TrainData_Features(TrainFile):
    #####################################################################################################
    # IMPORT LIBRARIES;
    #####################################################################################################
    import pandas, numpy as np, os, io, sys, pickle, pathlib, requests, pandas as pd
    from sklearn import preprocessing

    ###########################################################################################
    ## FILTER DATA
    ###########################################################################################
    colnames = ['age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country','income']
    dataFrame=pd.read_csv(TrainFile, sep=',', names=colnames, skipinitialspace=True, skip_blank_lines  = True, error_bad_lines = False, skiprows=1, na_values ='NaN').dropna()

    ## DROP SOME COLUMNS WHICH ARE IRRELEVANT OR DUPLICATED
    dataFrame = dataFrame.drop('fnlwgt', 1).drop('education', 1)
    
    ## FILTER DATA FOR COUNTRIES WHICH HAVE VERY FEW OBSERVATIONS IN TRAINING DATA (< 100), OR FOR WHICH COUNTRY IS UNKNOWN (?)
    country_filter = dataFrame.native_country.value_counts() > 100
    countrylist = list(pd.DataFrame(country_filter[country_filter == True]).axes[0])
    dataFrame = dataFrame[dataFrame['native_country'].isin(countrylist)]

    ## FILTER DATA UNKNOWN CATEGORIES OF workclass, marital_status, occupation, relationship, race, and sex
    dataFrame = dataFrame[~dataFrame.workclass.isin(list('?'))]
    dataFrame = dataFrame[~dataFrame.marital_status.isin(list('?'))]
    dataFrame = dataFrame[~dataFrame.occupation.isin(list('?'))]
    dataFrame = dataFrame[~dataFrame.relationship.isin(list('?'))]
    dataFrame = dataFrame[~dataFrame.race.isin(list('?'))]
    dataFrame = dataFrame[~dataFrame.sex.isin(list('?'))]
    dataFrame = dataFrame[~dataFrame.native_country.isin(list('?'))]

    # RESET INDICES FROM 0 to num_rows-1 
    dataFrame = dataFrame.reset_index(drop=True)

    ###########################################################################################
    ## TRANSFORM SOME FEATURES BY ENCODING OR STANDARDIZING FOR REGULARIZED REGRESSION METHODS
    ###########################################################################################
    # FIRST GET NUMERICAL AND CATEGORICAL COLUMNS TO ENABLE TRANSFORMATION
    catStringCols = ['workclass', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country'];
    numericCols = list(set(list(set(list(dataFrame.columns.values)) - set(catStringCols))) - set(['income']));
    
    # MAKE A COPY OF ORIGINAL 
    dataFrame_engineered = dataFrame[numericCols].copy();
     
    # Scale numerical values from train and test data
    for col in numericCols:
        dataFrame_engineered[col] = preprocessing.StandardScaler().fit_transform(dataFrame[col].astype(float).values.reshape(-1,1))

    # Convert string/categorical variables to one-hot encoded numerical variables
    for col in catStringCols:
        # Transform training data
        Enc_ohe, Enc_label = preprocessing.OneHotEncoder(), preprocessing.LabelEncoder();
        tmp_encoded_train = Enc_label.fit_transform(dataFrame[col]).reshape(-1,1)
        DF_dummies = pandas.DataFrame(Enc_ohe.fit_transform(tmp_encoded_train).todense(), columns = Enc_label.classes_)
        dataFrame_engineered = pandas.concat([dataFrame_engineered, DF_dummies], axis=1)

    # Add the target column into the data frame
    dataFrame_engineered = pandas.concat([dataFrame_engineered, dataFrame['income']], axis=1)

    # RETURN DataFrame
    return dataFrame_engineered


########################################################################################################
# FILTER AND TRANSFORM TEST DATA-SETS, WTIH REFERENCE TRANSFORMATIONS FIT TO TRAINING DATA
########################################################################################################
def filter_and_transform_TestData_Features(TestFile, TrainFile):
    #####################################################################################################
    # IMPORT LIBRARIES;
    #####################################################################################################
    import pandas, numpy as np, os, io, sys, pickle, pathlib, requests, pandas as pd
    from sklearn import preprocessing

    ###########################################################################################
    ## FILTER DATA
    ###########################################################################################
    colnames = ['age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country','income']
    train_df=pd.read_csv(TrainFile, sep=',', names=colnames, skipinitialspace=True, skip_blank_lines  = True, error_bad_lines = False, skiprows=1, na_values ='NaN').dropna()
    test_df=pd.read_csv(TestFile, sep=',', names=colnames, skipinitialspace=True, skip_blank_lines  = True, error_bad_lines = False, skiprows=1, na_values ='NaN').dropna()

    ## DROP SOME COLUMNS WHICH ARE IRRELEVANT OR DUPLICATED
    train_df = train_df.drop('fnlwgt', 1).drop('education', 1)
    test_df = test_df.drop('fnlwgt', 1).drop('education', 1)

    ## FILTER DATA FOR COUNTRIES WHICH HAVE VERY FEW OBSERVATIONS IN TRAINING DATA (< 100), OR FOR WHICH COUNTRY IS UNKNOWN (?)
    country_filter = train_df.native_country.value_counts() > 100
    countrylist = list(pd.DataFrame(country_filter[country_filter == True]).axes[0])
    train_df = train_df[train_df['native_country'].isin(countrylist)]
    test_df = test_df[test_df['native_country'].isin(countrylist)]

    ## FILTER DATA UNKNOWN CATEGORIES OF workclass, marital_status, occupation, relationship, race, and sex
    train_df = train_df[~train_df.workclass.isin(list('?'))]
    train_df = train_df[~train_df.marital_status.isin(list('?'))]
    train_df = train_df[~train_df.occupation.isin(list('?'))]
    train_df = train_df[~train_df.relationship.isin(list('?'))]
    train_df = train_df[~train_df.race.isin(list('?'))]
    train_df = train_df[~train_df.sex.isin(list('?'))]
    train_df = train_df[~train_df.native_country.isin(list('?'))]

    test_df = test_df[~test_df.workclass.isin(list('?'))]
    test_df = test_df[~test_df.marital_status.isin(list('?'))]
    test_df = test_df[~test_df.occupation.isin(list('?'))]
    test_df = test_df[~test_df.relationship.isin(list('?'))]
    test_df = test_df[~test_df.race.isin(list('?'))]
    test_df = test_df[~test_df.sex.isin(list('?'))]
    test_df = test_df[~test_df.native_country.isin(list('?'))]

    # # RESET INDICES FROM 0 to num_rows-1 
    train_df = train_df.reset_index(drop=True)
    test_df = test_df.reset_index(drop=True)

    ###########################################################################################
    ## TRANSFORM SOME FEATURES BY ENCODING OR STANDARDIZING FOR REGULARIZED REGRESSION METHODS
    ###########################################################################################
    # FIRST GET NUMERICAL AND CATEGORICAL COLUMNS TO ENABLE TRANSFORMATION
    catStringCols = ['workclass', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country'];
    numericCols = list(set(list(set(list(train_df.columns.values)) - set(catStringCols))) - set(['income']));

    # MAKE A COPY OF ORIGINAL 
    #train_df_engineered = train_df[numericCols].copy();
    test_df_engineered = test_df[numericCols].copy();
        
    # Scale numerical values from train and test data
    for col in numericCols:
        #train_df_engineered[col] = preprocessing.StandardScaler().fit_transform(train_df_engineered[col].astype(float).values.reshape(-1,1))
        test_df_engineered[col] = preprocessing.StandardScaler().fit(train_df[col].astype(float).values.reshape(-1,1)).transform(test_df[col].astype(float).values.reshape(-1,1))

    # Convert string/categorical variables to one-hot encoded numerical variables
    for col in catStringCols:
        # Transform training data
        Enc_ohe, Enc_label = preprocessing.OneHotEncoder(), preprocessing.LabelEncoder();
        tmp_encoded_train = Enc_label.fit_transform(train_df[col]).reshape(-1,1)
        #DF_dummies = pandas.DataFrame(Enc_ohe.fit_transform(tmp_encoded_train).todense(), columns = Enc_label.classes_)
        #train_df_engineered = pandas.concat([train_df_engineered, DF_dummies], axis=1)
        
        # Transform test data
        Enc_ohe, Enc_label = preprocessing.OneHotEncoder(), preprocessing.LabelEncoder();
        tmp_encoded_test = Enc_label.fit(train_df[col]).transform(test_df[col]).reshape(-1,1)
        DF_dummies = pandas.DataFrame(Enc_ohe.fit(tmp_encoded_train).transform(tmp_encoded_test).todense(), columns = Enc_label.classes_)
        test_df_engineered = pandas.concat([test_df_engineered, DF_dummies], axis=1)   

    # Add the target column into the data frame
    #train_df_engineered = pandas.concat([train_df_engineered, train_df['income']], axis=1) 
    test_df_engineered = pandas.concat([test_df_engineered, test_df['income']], axis=1) 

    # RETURN DataFrame
    return test_df_engineered