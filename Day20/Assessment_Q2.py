# Question: You have the following DataFrame:
# Write code to:
# data = {
#     "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
#     "Department": ["IT", "HR", "IT", "Finance", "HR"],
#     "Salary": [50000, 60000, 55000, 65000, 62000]
# }
# 1. Filter all employees from the "IT" department.
# 2.Find the average salary per department.
# 3. Add a new column "Salary_Adjusted" which increases each employee's salary by 10%

import pandas as pd
data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}
df=pd.DataFrame(data)
It_employees=df[df["Department"]=="IT"]
print("IT Department Employees\n")
print(It_employees)

avg_salary=df.groupby("Department")["Salary"].mean()
print("Average Salary")
print(avg_salary)

df["Salary_Adjusted"]=df["Salary"]*1.10
print("Salary Adjusted")
print(df)
