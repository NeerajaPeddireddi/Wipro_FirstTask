#Function Defination
from tarfile import ReadError
from typing import Iterator

from adodbapi import OperationalError


def add(a,b):
    print("Addition:",a+b)
add(1,2)
#using return
def sub(a,b):
    return  fr"Subtraction:{a-b}"
result=sub(5,3)
print(result)
from absl.testing.parameterized import parameters


# #  call by value and reference
def hello(greeting,name):
    print(greeting,name)
hello("Hello","Neeraja")
#no nee


def greet(greeting="Hello",name="Neeraja"):
    print(greeting,name)
greet()
# # calling one parameters
greet('Greetings','Neeraja')
greet("hi")
# # Single * gives output in tuple format -->(1, 2, 3, 4),accept any number of values
def print_params(*params):
    print(params)
print_params("Testing")
print_params(1,2,3,4)
#  ** gives output in dict format and takes 2 inputs like x=1 -->{'x': 1, 'y': 2, 'z': 3}
def print_params(**params):
    print(params)
print_params(x=1,y=2,z=3)

# modules import math and working in math functions
import math
print(math.sqrt(5))
print(math.floor(math.sqrt(5)))
print(math.pi)
print(math.pow(2,3))

# Creating class and initializing object then printing values
# without constructor
class Student:
    name="Neeraja"
    age=20
s1=Student()
print(s1.name)
print(s1.age)

# with constructor
class Employee():
    def __init__(self,name,age):
        self.name=name
        self.age=age

Employee.name="Neeraja"
Employee.age=20
print(Employee.name)
print(Employee.age)

# Built in iterator
data=[1,2,3]
it=iter(data)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Iterator   next
class NumberIterator:
    def __init__(self,number):
        self.number=number
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.number:
            value=self.current
            self.current+=1
            return value
        else:
            raise StopIteration
obj=NumberIterator(10)
print(next(obj))

# Generator
def number():
    yield 4
    yield 2
    yield 3
gen=number()
for i in gen:
    print(i)

# File Operations
# Read
file=open("f1.txt","r")
content1=file.read()
print(content1)
content=file.readline()
print(content)
content2=file.readlines()
print(content2)

#Append
file=open("f1.txt","a")

file.write("\nNew line added ")
file.close()

file=open("f1.txt","r")
content=file.read()
print(content)

#Write file it overrides the existing data
file=open("f1.txt","w")
file.write("Data1")
file.write("Data2")
file.close()

#Dumping data into json file
import json

data={
  "name": "neeru",
  "age": 22,
  "Skills": ["python","c"]
}
with open("f2.json","w") as file:
   json.dump(data,file,indent=4)

#Now writing into csv file
import csv
with open("f3.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Sno","Name","Age"])
    writer.writerow(["1", "A", "24"])
    writer.writerow(["2", "B", "22"])
#reading data from xml file and creating new xml file with code and insert data into that
import xml.etree.ElementTree as ET

tree = ET.parse("student.xml")
root = tree.getroot()

for stu in root.findall("student"):
    Id = stu.find("id").text
    name = stu.find("name").text
    marks = stu.find("marks").text
    print(Id, name, marks)

root=ET.Element("employee")
emp1=ET.SubElement(root,"emp")
ET.SubElement(emp1,"id").text="101"
ET.SubElement(emp1,"name").text="chand"
ET.SubElement(emp1,"marks").text="93"
emp2 = ET.SubElement(root, "emp")
ET.SubElement(emp2, "id").text = "102"
ET.SubElement(emp2, "Name").text = "pavi"
ET.SubElement(emp2, "Salary").text = "200000"


tree = ET.ElementTree(root)
tree.write("employee.xml")
print("xml file written successfully")

#Decorators
def mydecorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
@mydecorator
def say_hello():
    print("Hello")
say_hello()
#descriptors get,set,delete
class mydescriptor:
    def __get__(self, obj, owner):
        print("Getting value")
        return obj._x
    def __set__(self, obj, value):
        print("Setting value")
        obj._x=value
class Test:
    x=mydescriptor()
t=Test()
t.x=10
print(t.x)
#enumarate
fruits=["apple","banana","orange","mango"]
for index,fruit in enumerate(fruits):
    print(index,fruit)

#Sending the fixed values
from enum import Enum
class Fruits(Enum):
    apple=1
    orange=2
print(Fruits.apple.name)
print(Fruits.apple.value)