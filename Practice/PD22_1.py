import mysql
from mysql import connector
from mysql.connector import cursor

hostname="localhost"
user="root"
password="Neeru@489"
database="feb2026"

connection=mysql.connector.connect(host=hostname, user=user, password=password, database=database)
cursor=connection.cursor()
print("Connected to MySQL database")

query="select * from employee"
cursor.execute(query)
res=cursor.fetchall()
for row in res:
    print(row)