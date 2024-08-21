import pandas as pd
#first of all we are going to see insert fun in pandas
var=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
print(var)
#in insert function you have to give three parameters first for index,name and postion of new coloumn,what data you want to insert.
var.insert(2,"C",[6,7,8,9,10])#but the length of your coloumns must be equal
print(var)
#let see a logic here if you want to insert one more same coloumn in your datafram so you have to copy the
#coloumn and you dont want all the data you just wanted limited data in your this new coloumn so how would you do that?
var["D"]=var["A"][:3]#here i am going to do slicing in list.
print(var)
#now we are going to see delete fun in pandas.
var1=pd.DataFrame({"zee":[1,2,3,4],"zax":[1,2,3,4]})
print(var1)
var1.pop("zax")#pop fun is used to delete the column.
print(var1)
