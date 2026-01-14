# Question – Descriptors
# Topic: Descriptors
# Create a class Employee with attributes:
# name
# salary
# 1. Ensures salary is always a positive number
# 2. Raises a ValueError if a negative salary is assigned
# 3. Demonstrates the descriptor by creating multiple Employee objects

class SalaryDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = "_"+name
    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        setattr(instance, self.private_name, value)
class Employee:
    salary=SalaryDescriptor()
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
e1=Employee("Arun",8000)
print(e1.name)
print(e1.salary)
e2=Employee("Rama",-70000)
print(e2.name)
print(e2.salary)