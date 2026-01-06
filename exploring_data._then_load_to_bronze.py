##importing library to work with tables 
import pandas as pd

### read csv file 
df=pd.read_csv("pc_data.csv", sep=";")
print(df)

df.to_csv("bronze_pc_data.csv", index=False)
print("Bronze layer created")

## check the first few rows 
print(df.head())

##checking how many columns and rows in the dataset
print(df.shape)

##checking data types.
print(df.dtypes)

##check missing values 
print(df.isnull().sum())

## checks distinct values in the Continent column and check the consistency 
Continents = (df["Continent"].unique())
print(f"These are the Continents in this column {Continents}")

##Define columns not to be excluded when printing distinct values for each column 
exclude_columns = ["Customer Contact Number",
"Customer Email Address",      
"Sales Person Name",           
"Sales Person Department","Ship Date", "Purchase Date", "Customer Surname","Customer Name",  "PC Model","Province or City"]

##This checks only objects columns, exlude the columns I dont want to see and find distinct values
##Go through each text column in the dataset, and get unique values, removes missing values then print each value as a bullet point
for col in df.select_dtypes(include="object").columns:
    if col not in exclude_columns:
        print(f"\nUnique values in column: {col}")
        for value in df[col].dropna().unique():
            print("-", value)




