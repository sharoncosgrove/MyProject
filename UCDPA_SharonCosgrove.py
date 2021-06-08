import pandas as pd

data = pd.read_csv("forbes_billionaires.csv")

missing_val=data.isnull().sum()
print(missing_val)

print(data.info())

print(data.describe())

