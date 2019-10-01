# practice a simple ML data set 
# used tutorial on this site: 
# https://www.hackerearth.com/practice/machine-learning/data-manipulation-visualisation-r-python/tutorial-data-manipulation-numpy-pandas-python/tutorial/
# data is from UCI Machine Learning Repository

import pandas as pd
from sklearn import preprocessing

#load the data
train  = pd.read_csv("datafiles/train.csv")
test = pd.read_csv("datafiles/test.csv")

#check data set
train.info()

#check number of rows and columns
print ("The train data has",train.shape)
print ("The test data has",test.shape)

# check for missing values in data set
nans = train.shape[0] - train.dropna().shape[0]
print ("%d rows have missing values in the train data" %nans)

nand = test.shape[0] - test.dropna().shape[0]
print ("%d rows have missing values in the test data" %nand)

#only 3 columns have missing values
train.isnull().sum()

# count the unique values from character variables
cat = train.select_dtypes(include=['O'])
cat.apply(pd.Series.nunique)

# impute missing values with respective modes

#Education
train.workclass.value_counts(sort=True)
train.workclass.fillna('Private',inplace=True)


#Occupation
train.occupation.value_counts(sort=True)
train.occupation.fillna('Prof-specialty',inplace=True)


#Native Country
train['native.country'].value_counts(sort=True)
train['native.country'].fillna('United-States',inplace=True)

#check that now there aren't any missing values
train.isnull().sum()
# check for missing values in data set
nans = train.shape[0] - train.dropna().shape[0]
print ("%d rows have missing values in the train data" %nans)

#investigate if data is imbalanced
#check proportion of target variable
train.target.value_counts()/train.shape[0]

#creat cross tab of the target variable with education
pd.crosstab(train.education, train.target,margins=True)/train.shape[0]
# see that now all the columns have the same amount of data
train.info()

#view head before
print(train.head())

#load sklearn and encode all object type variables
# creat a model for numbering string variables
for x in train.columns:
	if train[x].dtype == 'object':
		lbl = preprocessing.LabelEncoder()
		lbl.fit(list(train[x].values))
		train[x] = lbl.transform(list(train[x].values))
# view after changes of numeric conversion
print("new:")
print(train.head())

