import pandas as pd
x=[3,4,5]
var=pd.Series(x,index=["a","b","c"])
print(var)
#you can also change the index number
#now we are going to see how can pandas work with the dictionary
dic={"name":["python","c","c++","java"],"por":[12,13,14,15],"Rank":[1,4,3,2]}
var1=pd.Series(dic)
print(var1)
s1=pd.Series(12,index=[1,2,3,4,5,6,7,8])
print(s1)
s2=pd.Series(12,index=[1,2,3,4])
print(s2)
print(s1+s2)#here is the reason why we used pandas insted of using numpy because in numpy it will give
#us an broadcstionf error because of not equal indexes on both side but in pandas it also works with the empty data sets



