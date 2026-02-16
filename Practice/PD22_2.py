from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db=client["company_db"]
collection=db["employees"]

new_employee={
    "name":"Rani",
    "department":"IT",
    "salary":"50000",
}
insert_result = collection.insert_one(new_employee)
print("Inserted new employee with ID:",insert_result.inserted_id)

print("new employee",collection.find_one({"_id":insert_result.inserted_id}))
