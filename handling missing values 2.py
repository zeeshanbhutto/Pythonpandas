#how to handle missing data in axcel sheet through pandas we are going to see through replace fun.
import pandas as pd
var=pd.read_csv("C:\\Users\\3tee\\PycharmProjects\\pandaspractice\\test_new3.csv")
print(var)
print(var.replace(to_replace=15,value=22))#by this you can replace your int value.
print(var.replace(to_replace=13,value="bhutto"))#by this you can also replace string values.
print(var.describe())#just for fun
print(var.replace("[A-Za-z]","python",regex=True))
print(var.replace({"zeeshan":"[a-z]"},"22",regex=True))#this will replace your any alphabetical value from other.

print(var.interpolate())#this function only work with numwric values .
print(var.interpolate(method="linear"))