import pandas as pd
var1=pd.DataFrame({"A":[1,2,3,4],"B":[12,22,32,24]})
var2=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
print(pd.merge(var2,var1,on="A"))#this is how you can merge to dataframes and only comman part of data will be merged.
print(pd.merge(var1,var2,how="left"))
print(pd.merge(var1,var2,how="right"))
print()
print(pd.merge(var1,var2,how="outer"))