from importlib.metadata import files

from zmq.green import device
from zmq.ssh import paramiko_tunnel


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

# The subprocess module allows a Python program to execute
# operating system commands and interact with their input, output, and errors.

#to echo some thing we use this below code in python
#in cmd we use echo"hello world"
# Python → talks to the operating system
# 👉 run operating system (OS) commands
# 👉 run other programs/scripts
# 👉 communicate with them
import subprocess
result=subprocess.run(
    ["echo", "Hello World"],
    capture_output=True,
    text=True,
    shell=True,

)
print(result.stdout)

#Subprocess run in single line
import subprocess
# subprocess.run(("python","Assessment_Q1.py"))
#output execute above pyton file print the output same like cmd pyton filename.py
#to print ls
import subprocess
resultls = subprocess.run(
    ["dir"],
     shell=True,
     capture_output=True,
     text=True)
print(resultls.stdout)

#Threading
import threading
def task1():
    print("Task 1")
t=threading.Thread(target=task1)
t.start()
t.join()
print("Main thread ends")

#Virtual Environment
#A virtual environment is a self-contained directory that contains its own Python
# interpreter and libraries, isolated from the system Python.
#if project A -->need python 3.0
#if project B -->need python 3.3
# then we use this virtual env
# create env
# python -m venv myenv
# Activate
# myenv\Scripts\activate
# Deactivate
# deactivate
# How to Check Active Virtual Environment
# where python
#pip install selenium


# Remote host\device  using paramiko
# what is paramiko?
# connect to a remote machile\device
# using ssh(Secure Shell)
# Execute commands remotely
# Transfer files()
# Your Python program → connects to another computer → runs commands there
#
# remote host-->another device.linux system,cloud virtual machine
# youneed -->idaddress,username,password,ssh keys
