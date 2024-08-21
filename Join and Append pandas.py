import pandas as pd
var1=pd.DataFrame({"A":[1,2,3,4,5],"B":[6,7,8,9,10]},index=["a","b","c","d","e"])
var2=pd.DataFrame({"C":[11,12,13],"D":[16,17,18]},index=["a","b","c"])
print(var1.join(var2))
#one think i want to make it clear here that if your column name are same it will show you an
#error but  let suppoae you are getting an error how you will fix it? ok let see....
var3=pd.DataFrame({"E":[1,2,3,4,5],"G":[6,7,8,9,10]})
var4=pd.DataFrame({"F":[11,12,13,14,15],"G":[16,17,18,19,20]})
print(var3.join(var4,how="inner",lsuffix="_12"))
#now we are going to see append fun in pandas
var1=pd.DataFrame({"A":[1,2,3,4,5],"B":[6,7,8,9,10]})
var2=pd.DataFrame({"C":[11,12,13,14,15],"D":[16,17,18,19,20]},)
print(var1._append(var2,ignore_index=True))