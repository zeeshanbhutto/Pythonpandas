#CSV format is a plan text format in which values are seprated by commas,
import pandas as pd
dis={"a":[19,20,13,14,15],"b":[11,12,31,14,15],"c":[11,12,23,34,15],"subject":[1,2,3,4,5]}
var=pd.DataFrame(dis)
print(var)
var.to_csv("test_new3.csv",index=False,header=["zeeshan","Rehan","jamshed","subject"])