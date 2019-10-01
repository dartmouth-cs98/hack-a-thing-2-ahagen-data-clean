# practice a simple ML data set 
# used tutorial on this site: 
# https://www.hackerearth.com/practice/machine-learning/data-manipulation-visualisation-r-python/tutorial-data-manipulation-numpy-pandas-python/tutorial/
# data is from UCI Machine Learning Repository

import pandas as pd

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