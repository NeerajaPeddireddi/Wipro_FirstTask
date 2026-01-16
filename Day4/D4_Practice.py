class Student:
    def display(self):
        print("hello world")
obj=Student()# Object creation
obj.display() #calling

#parametrized method
class Calculator:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
obj1=Calculator
print(obj1.add(2,3))
print(obj1.sub(4,5))

#constructors and destructors
class employee:
    def __init__(self):
        print("constructor called")

    def __del__(self):
        print("destructor called")
obj=employee()
#when object is created constructor and destructor both are called
# output
# constructor called
# destructor called

#Parametrized constructor
class employee1:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
obj1=employee1("James",5000)
print(obj1.name,obj1.salary)

#Abstaction
from abc import ABC,abstractmethod #ABC-->Abstract Base Class,Decorator
class Shape(ABC):#inside () ABC tells abstact class this is
    #Declaring an Abstract Method,No implementation
    @abstractmethod
    def area(self):
        pass
#Creating a child class
class Rectangle(Shape):
    #Implementing abstract method
    def area(self):
        print("area method implemented")
#Object creation and method call
r=Rectangle()
r.area()
#output
#area method implemented

#Abstraction along with constructor
from abc import ABC,abstractmethod #ABC-->Abstract Base Class,Decorator
class Employee(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def salary(self):
        pass
class Person(Employee):
    def salary(self):
        print(self.name,"salary is 4000")
obj=Person("Neeru")
obj.salary()

#Multiple abstract methods and their implementation
from abc import ABC,abstractmethod
class BANK(ABC):
    @abstractmethod
    def interest(self):
        pass
    @abstractmethod
    def loan(self):
        pass

class SBI(BANK):
    def interest(self):
        print("interest is 6%")
    def loan(self):
        print("loan is available")

s=SBI()
s.interest()
s.loan()