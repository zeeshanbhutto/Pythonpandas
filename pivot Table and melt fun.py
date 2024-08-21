import pandas as pd
var=pd.DataFrame({"Days":[1,2,3,4,5,],"eng":[10,12,14,16,18],"maths":[17,18,16,13,16]})
print(var)
print(pd.melt(var,id_vars=["Days"],var_name="Subject",value_name="Marks"))#it will create one think unique which you want.
#now we are going to see pivot fun in pandas
var=pd.DataFrame({"Days":[1,1,1,2,2,],"Stud_name":["zeeshan","Basit","MAzhar","zafar","Jabar"],"eng":[10,12,14,16,18],"maths":[17,18,16,13,16]})
print(var)
#Basically pivot and melt fun is used to reshape the Tables in pands which helps to understanding of data.
print(var.pivot(index="Days",columns="Stud_name"))
print()
print(var.pivot_table(index="Stud_name",columns="Days",aggfunc="sum",margins=True))