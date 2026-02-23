#Inheritance
class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def bark(self):
        print("Dog makes a bark")
obj=Dog()
obj.speak()
obj.bark()

#Multiple Inheritance
class A:
    def showA(self):
        print("A")
class B:
    def showB(self):
        print("B")
class C(A,B):
    print("A from class B")
c=C()
c.showA()
c.showB()

#Multilevel Inheritance
class A:
    def showA(self):
        print("A")
class B(A):
    def showB(self):
        print("B")
class C(B):
    def showC(self):
        print("C")
c=A()
c.showA() #-->Executed gives only A not B,C
c.showB()
c.showC()

c=B()
c.showA() #-->Executed gives A,B not C
c.showB()
c.showC()

c=C()
c.showA() #-->Executed gives A,B,C
c.showB()
c.showC()

#Hierarchical Inheritance
class Parent:
    def parent(self ):
        print("Parent1")
class Child1(Parent):
    def child1(self):
        print("Child1")
class Child2(Parent):
    def child2(self):
        print("Child2")
obj=Child1()
obj.parent()
obj.child1()
obj.child2()


#Polymorphism
#run time-->overriding and compile time-->overloading
#__add__ this function will call when + is called
class box1:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return self.value + other.value
b1=box1(5)
b2=box1(6)
print(b1+b2)

#method overriding
class animal:
    def sound(self):
        print("Animal Sound")
class dog(animal):
    def sound(self):
        print("Dog Sound")
class cat(animal):
    def sound(self):
        print("Cat Sound")
obj=[dog(),cat()]
for a in obj:
    a.sound()

#Method overloading
# “Here only ONE method exists. Python is not choosing between methods.”
# Python is not selecting different methods
# # It is just using default values
# Python does NOT support true method overloading
class calc:
    def add(self,a,b=0,c=0):
        return a+b+c

cal=calc()
print(cal.add(2,3))
print(cal.add(2,3,4))

class Calc:
    def add(self, *params):
        total = 0
        for x in params:
            total += x
        return total


c = Calc()
print(c.add(2, 3))
print(c.add(2, 3, 4))
print(c.add(1, 2, 3, 4, 5))

#Constructor overloading is not supported in python
# Super() keyword -->refers the parent class
class Parent():
    def greeting(self):
        print("Hello parent")
class Child(Parent):
    def greeting(self):
        print("Hello child")
        super().greeting()
c=Child()
c.greeting()
