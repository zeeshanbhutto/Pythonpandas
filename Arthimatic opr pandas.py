import pandas as pd
#the logic is that is we are going to create a dataframe were we are going to create a dictionary in that
#dic we are going to take tow coloumns and then add them and there answer will be in the third coloumn.
var=pd.DataFrame({"A":[1,2,3,4,5],"B":[5,6,7,8,9]})
print(var)
var["C"]=var["A"]+var["B"]
print(var)
var=pd.DataFrame({"A":[1,2,3,4,5],"B":[5,6,7,8,9]})
print(var)
var["C"]=var["A"]-var["B"]
print(var)
var["C"]=var["A"]*var["B"]
print(var)
var["C"]=var["A"]/var["B"]
print(var)
var1=pd.DataFrame({"A":[10,11,12,13,14],"B":[15,16,17,18,19]})
print(var1)
var1["D"]=var1["A"]<13
var1["E"]=var1["B"]<19
print(var1)