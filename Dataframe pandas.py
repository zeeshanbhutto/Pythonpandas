import pandas as pd
l=[1,2,3,4,5,6,7]
var=pd.DataFrame(l)
print(var)
#now we are going to see that how we can create a dtaframe through pandas.
d={"A":[1,2,3,4,5],"B":[1,2,3,4,5],"C":[11,22,33,44,55]}
var1=pd.DataFrame(d,index=["a","b","c","d","e"],columns=["A","C"])#you can also espacifically choice  which coloumn or row of the data frame you want.
print(var1)#your length must be same in this case.
#let see how to get the dat of any row any colums
print(var1["C"]["c"])
#now see how to create a list in 2D array
list_1=[[1,2,3,4,5],[11,22,33,44,55]]
var2=pd.DataFrame(list_1)
print(var2)
#how to get from dictionary in series in pandas
sr={"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,4])}
var3=pd.DataFrame(sr)#from two series combination we have created a dataframe in pandas
print(type(var3))
print(var3)