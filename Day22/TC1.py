import mysql.connector

host="localhost"
user="root"
password="Neeru@489"
database="feb2026"

connection=mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor=connection.cursor()
print("Connected to MySQL database")

query="select * from employee";
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)