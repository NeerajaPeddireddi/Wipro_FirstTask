import pandas as pd
import numpy as np

from Day22.Assessment_Q2 import product_quantity, best_selling_product

# load
df=pd.read_csv("sales.csv")
print(df)

# New column

df["Total"]=df["Quantity"]*df["Price"]
print(df)

# numpy
total_values=df["Total"].values
total_sales=np.sum(total_values)
print(total_sales)
total_avg=np.mean(total_values)
print(total_avg)
total_std=np.std(total_values)
print(total_std)

# best selling product

product_quantity=df.groupby("Product")["Quantity"].sum()
print(product_quantity)
best_selling_product=product_quantity.idxmax()
print(best_selling_product)