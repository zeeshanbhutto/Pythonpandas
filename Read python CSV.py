#A simple way to store big data sets is to use CSV file (comma seprated files.) csv file contain plain text
# and it is a well known platform that can be ready by every one including pandas.
import pandas as pd
csv_1=pd.read_csv("C:\\Users\\3tee\PycharmProjects\\pandaspractice\\test_new3.csv")
print(csv_1)
#now here i have learned that how to open or read a csv file and now i am going to learned to work with data.
csv_2=pd.read_csv("C:\\Users\\3tee\PycharmProjects\\pandaspractice\\test_new3.csv",nrows=3)
print(csv_2)
csv_3=pd.read_csv("C:\\Users\\3tee\PycharmProjects\\pandaspractice\\test_new3.csv",usecols=["subject","zeeshan"])
print(csv_3)
csv_1=pd.read_csv("C:\\Users\\3tee\PycharmProjects\\pandaspractice\\test_new3.csv",skiprows=[1])
print(csv_1)
csv_1=pd.read_csv("C:\\Users\\3tee\PycharmProjects\\pandaspractice\\test_new3.csv",index_col=["zeeshan"])
print(csv_1)
csv_1=pd.read_csv("C:\\Users\\3tee\PycharmProjects\\pandaspractice\\test_new3.csv",header=1)
print(csv_1)
csv_1=pd.read_csv("C:\\Users\\3tee\PycharmProjects\\pandaspractice\\test_new3.csv",names=["english","urdu","maths","physics"])
print(csv_1)


