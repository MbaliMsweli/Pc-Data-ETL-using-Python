import pandas as pd

### read csv file 
df=pd.read_csv("pc_data.csv", sep=";")
print(df)

## check the first few rows 
print(df.head())

##checking how many columns and rows in the dataset
print(df.shape)

##checking data types 
print(df.dtypes)

##check missing values 
print(df.isnull().sum())