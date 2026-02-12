from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
collection = db["employees"]

print("Connected to MongoDB")

new_employee={
        "name":"Ram",
        "department":"CSE",
        "salary":100000
}

collection.insert_one(new_employee)
print("\nEmployee inserted successfully")

print("\nEmployees in IT Department")
it_employee = collection.find({"name":"IT"})
for emp in it_employee:
    print(emp)

employee_name="Ram"
collection.update_one(
    {"name":employee_name},
    {"$mul":{"salary":1.10}},
)
print("\nEmployee updated successfully")