import pandas as pd
var=pd.read_csv("C:\\Users\\3tee\\PycharmProjects\\pandaspractice\\test_new3.csv")
print(var)
print()
print(var.dropna())
print(var.dropna(axis=1))#will work along columns
var1=pd.read_csv("C:\\Users\\3tee\\PycharmProjects\\pandaspractice\\test_new3.csv")
print(var1.dropna(how="all"))#in this particular case one all nun row will be droped.
var1=pd.read_csv("C:\\Users\\3tee\\PycharmProjects\\pandaspractice\\test_new3.csv")
print(var1.dropna(how="any"))#in this particular case if there will any singlr value nun it will be droped all row.
print(var1.dropna(subset=["Rehan"]))#this will only drop data according to particular access of column.
print()
print(var1.dropna(inplace=True))#it will drop your all null values and create a new dataframe
print(var1.dropna(thresh=1))#it will drop only those row in which no of null values you give.
print(var.fillna("python"))#this will fill your empty values wiith required value you give.
print(var.fillna({"Rehan":13,"jamshed":15}))#if you want to fill particular data with respect to time than you should create a dic and follow the same fun.
