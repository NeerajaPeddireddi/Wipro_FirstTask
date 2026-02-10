import numpy as np
import pandas as pd
arr=([10,20,30,40,50,60,70,80,90,100])
print(np.array(arr))
print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.multiply(arr,2))

data={
    "Name":["Ram","Bheem","Dharm"],
    "Age":[21,22,23],
    "City":["Hyderabad","Bangalore","chennai"]
}
df=pd.DataFrame(data)
print(df)
print(df.describe())
print(df["Name"])
print(max(df["Age"])) #max age
print(df["Age"]>20)

