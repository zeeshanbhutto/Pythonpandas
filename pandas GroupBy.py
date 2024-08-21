#group by is a function in pandas which is usually used to make data in sequence,
import pandas as pd
var=pd.DataFrame({"name":["a","b","c","d","a","b","c","d"],"sub_1":[10,11,12,13,14,15,16,17],
                  "sub_2":[21,22,23,24,25,26,27,28]})
print(var)
var_new=var.groupby("name")
print(var_new)#here your data is groupby and store in this variable but could'nt shown to see the data we have to use loop

for x,y in var_new:
    print(x,y)
print()

print(var_new.get_group("a"))#by doing this you will get min data which you have group

print(var_new.min())
print()
print(var_new.max())

li=list(var_new)#by doing this you can get your data in list
print(li)