import pandas as pd
import numpy as np

#1. Load the CSV into a Pandas DataFrame.
df=pd.read_csv("sales.csv")
print(df)

# 2. Add a new column "Total" which is Quantity * Price.
df["Total"]=df["Quantity"]*df["Price"]
print("\nData With Total Column")
print(df)

#3. Using NumPy, calculate the total sales, average daily sales, and standard deviation of daily sales.
total_values=df["Total"].values
total_sales=np.sum(total_values)
average_sales=np.mean(total_values)
std_sales=np.std(total_values)

print("\nSales Statistics")
print("Total Sales:",total_sales)
print("Average Sales:",average_sales)
print("Standard Deviation Sales:",std_sales)

# 4. Find the best-selling product based on total quantity sold.
product_quantity=df.groupby("Product")["Quantity"].sum()
print("Product Quantity:",product_quantity)
best_selling_product=product_quantity.idxmax()
print("\nBest Selling Product:",best_selling_product)