#2 Importing Data
import pandas as pd

data = pd.read_csv("forbes_billionaires.csv")

#3 Analysing Data - To be able to see missing data
missing_val=data.isnull().sum()
print(missing_val)

#3 Analying Data - The info() function is used to print a concise summary of a DataFrame such as column name and type
print(data.info())

#3 Analysing Data - Describe is used to view statistical details like percentages, min and max figures
print(data.describe())

#To replace the gaps with "*"
cleaned_data=data.fillna("*")
missing_val=cleaned_data.isnull().sum()
print(missing_val)

#To replace the gaps with mean
cleaned_data=data.fillna(data.mean)
missing_val=cleaned_data.isnull().sum()
print(missing_val)

