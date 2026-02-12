import mysql.connector

host="localhost"
user="root"
password="Neeru@489"
database="company_db"

connection=mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor=connection.cursor()
print("Connected to MySQL database")

#create table
create_table_query="""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    department VARCHAR(255),
    salary FLOAT
)
"""
cursor.execute(create_table_query)
print("\nTable created successfully")
#Insert new employee

insert_query="""
INSERT INTO employees (name, department, salary) 
VALUES (%s, %s, %s)
"""
employee_data1=("Ram","IT",60000)
employee_data2=("Seetha","IT",30000)
cursor.execute(insert_query, employee_data1)
cursor.execute(insert_query, employee_data2)
connection.commit()
print("\nTable inserted successfully")

#get employees
fetch_query="select * from employees where salary>50000"
cursor.execute(fetch_query)
print("\nEmployees with salary less than 50000:")
for row in cursor.fetchall():
    print(row)

#Update salary by 10%
# Update salary by 10% using name
employee_name = "Ram"

update_query = """
UPDATE employees
SET salary = salary * 1.10
WHERE name = %s
"""

cursor.execute(update_query, (employee_name,))
connection.commit()

print("Salary updated successfully")

# delete_query = "DELETE FROM employees"
# cursor.execute(delete_query)
# connection.commit()
# print("\nEmployees deleted successfully")
#close connection
cursor.close()
connection.close()
print("\nConnection closed")