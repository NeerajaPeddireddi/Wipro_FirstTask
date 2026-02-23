from math import *

from jupyter_server.auth import passwd

#simple python code
print("Hello")

#Taking input from user
x=input("Enter Your Age")
if(int(x)>18):
    print("Eligible for Vote")
else:
    print("Not Eligible for Vote")

#Variables
_x=10
print(_x)

#Arithmetic operations
a=10
b=20
print("Addition",a+b)
print("Subtraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)
print("Modulo",a%b)
print("Floor Division")

#Builtin Operations
import math
print(math.sqrt(4))
print(math.log(1))
print(math.exp(2))
print(math.lgamma(3))
print(math.e)

#comparision
a=20
b=30
if(a==b):
    print("Both are equal")
else:
    print("Both are not equal")

#String Operations
a="Neeraja"
#slicing
print(a[0])
#Negatie Indexing
print(a[-5])
#multiple line through triple quotes
str=("""hello
        world
     """
     )
print(str)
#range
print(a[0:5])
#reverse of string
print(a[::-1])
#concatination
print("helo"+" "+a)
#replace
print(str.replace("world","india"))
#convert to upper
print(a.upper())
#length
print(len(a))
#finding char is present or not
print("n" in a)
print("N" in a)
#format
str1="I am {} I am from {}".format("Neeraja","AP")
print(str1)
#split
str2=str1.split()
print("Splitted String",str2)

#List
num=[1,2,3,4,5]
names=["arun","bhanu","charanya","dolly"]
mix_list=[1,"a",1.2,"ram"]
print(num)
print(names)
print(mix_list)

for i in num:
    print(i)
for j in mix_list:
    print(j)
if 10 in num:
    print(num.index(10))
else:
    print(num.count(10))
#nested list
print(num,names)
#matrix
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])
#reverse
names.reverse()
print(names)
#append
names.append("elon")
print(names)
#extend
names.extend(a)
print(names)
#remove
names.remove("elon")
print(names)
#insert
names.insert(0,"sana")
print(names)

#tuples
t1=(1,2,2,3)
t2="ram","raj","arun"
print(t1)
print(t2)
#slicing
print(t1[0])
print(t2[-1])
print(t1[0:4])
#assining not possible in tuple because it is immutable
#t1[3]=40
print(t1)
#count
print(t1.count(2))
#index
print(t1.index(3))
#nested tuple
print(t1,t2)

#swaping
a=10
b=2
a,b=b,a
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)

data=10,20,30
a,b,c=data
print(a,b,c)

#dictionary
dict1={1:2,2:4,3:6,4:8}
print(dict1)
#tuple as key in dict
dict2={(1,2):"a",(3,4):"b"}
print(dict2)
#getting values
print(dict2.values())
#getting keys
print(dict2.keys())
#update,assign
dict1[1]=10
print(dict1)
print(dict1.popitem())
print(dict1)

for key in dict2:
    print(key,dict2[key])
#nested dict
emp={
    101:{"name":"manu","salary":2000},
    102:{"name":"archu","salary":1000}
}
print(emp)
#get
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

print(student.get("name"))

#set
set1={1,2,3,4,1,2,3,4}
print(set1)
for i in set1:
    print(i)
#adding
set1.add(5)
print(set1)
set1.add(5)
print(set1)

A={1,2,3}
B={3,4,5}
print(A|B)#Union
print(A&B)#Intersection

#mutiple assignment
a=b=2

#control structures
#If,elif,else,for,while-->do while not possible in python
num=5
if num%2==0:
    print("even")
else:
    print("odd")
marks=80
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
else:
    print("Grade C")
#for loop
for i in range(1,6):
    print(i)
j=1
while j<=5:
    print(j)
    j=j+1
#Switch
day=2
match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
#break
j=1
while j<=5:
    print(j)
    if j==2:
        print("break",j)
        break
    j=j+1
#lambda function
add=lambda a,b:a+b
print(add(10,20))

#multiplication using lambda function
mul=lambda a,b:a*b
print(mul(10,20))
#maxnumber using lambda function
maxnum = lambda a,b:a if a>b else b
print(maxnum(10,20))
#map function iterable
numbers=[1,2,3,4,5]
result=list(map(lambda x:x**2,numbers))
print(result)

#Exception handling
#Zero Division Eror
a=10
b=5
try:
    div=a/b
    print(div)
except ZeroDivisionError:
    print("division by zero")
except Exception as e:
    print(e)

#Perfect root or not with negative values
x=int(input("Enter num:"))
try:
    res=math.sqrt(x)
    print(res)
except ValueError:
    print("ValueError")
except Exception as e:
    print(e)
#User Defined Exception
# class myError(Exception):
#     pass
# raise myError("This is a user defined Error")
class InvalidAge(Exception):
    pass
try:
    age=int(input("Enter age:"))
    if age<18:
        raise InvalidAge("Age must be less than or equal to 18")
    else:
        print("Eligible age")
except InvalidAge as e:
    print("Error",e)
