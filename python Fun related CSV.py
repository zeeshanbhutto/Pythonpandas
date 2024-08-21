import pandas as pd
csv_1=pd.read_csv("C:\\Users\\3tee\PycharmProjects\\pandaspractice\\test_new3.csv")
print(csv_1)
print(csv_1.index)#this is how you can find the index of csv file..............
print(csv_1.columns)#this is how you can get the coloumn names....
print(csv_1.describe())#where you will get all the int values and known the min max and mean values...
print(csv_1.head(2))
print(csv_1.tail(2))
#we can also used list slicing here to get the data of particular rows.
print(csv_1[3:4])
print(type(csv_1))
print(csv_1.index.array)

print(csv_1.to_numpy())
print(csv_1.sort_index(axis=0,ascending=False))

csv_1["Rehan"][0]="Rara"#thins methoad is not suitable for creating changes in your dataframe insted you can use loc fun to create changes.
print(csv_1)

csv_1.loc[0,"Rehan"]="Rara"
print(csv_1)

var = csv_1.loc[[2, 3], ["zeeshan", "Rehan"]]
print(var)#to get the particular data from the dataframe..


var = csv_1.loc [:,["zeeshan", "Rehan"]]
print(var)#if you want to get all the particular data from particular column of the dataframe..

r=csv_1.iloc[0,1]
print(r)
s=csv_1.iloc[0,2]
print(s)

d=csv_1.drop("Rehan",axis=1)
print(d)





