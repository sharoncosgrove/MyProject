import pandas as pd

data = pd.read_csv("forbes_billionaires.csv")
print(data.info())

print(data.describe())

