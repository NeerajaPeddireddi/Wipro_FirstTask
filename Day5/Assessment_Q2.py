# Question – Polymorphism (Method & Operator Overloading)
# Topics: Introduction to Polymorphism, Polymorphism on Operators
# 2.Create  another class AdvancedCalculator that overrides a method from Calculator
# 3.Implement operator overloading by overloading the + operator to add two objects of a custom class
# 4.Demonstrate polymorphism using the same method name with different behaviors

# 1. Create a class Calculator that demonstrates method overriding
class Calculator:
    def add(self,a,b):
        return a+b
class Child(Calculator):
    def add(self,a,b):
        return f"addition {a}+{b} is:{a+b}"
obj = Child()
print(obj.add(5,6))

# 2.Create  another class AdvancedCalculator that overrides a method from Calculator
class AdvancedCalculator(Calculator):
    def add(self,a,b):
        return f"Advanced calci result:{a+b}"
obj = AdvancedCalculator()
print(obj.add(5,6))

# 3.Implement operator overloading by overloading the + operator to add two objects of a custom class
class box1:
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return self.num + other.num
b1=box1(7)
b2=box1(6)
print("Sum is:", b1+b2)

# 4.Demonstrate polymorphism using the same method name with different behaviors
class Parent:
    def Greeting(self):
        print("Hello")
class child(Parent):
    def Greeting(self):
        print("Welcome to my World")
c=child()
c.Greeting()