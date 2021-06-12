import pandas as pd

def myfunc():
    print ("My Function")

def importdata(filename):
    data=pd.read_csv(filename)
    return data

data=importdata("forbes_billionaires.csv")
print(data)


