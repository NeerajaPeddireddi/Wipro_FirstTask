# Question – Class Types & Inheritance
# Topics: Class types, Introduction to Inheritance, Types of Inheritance
# 1. Create a base class Vehicle with a method start()
# 2.Create a derived class Car that inherits from Vehicle
# 3.Add a class variable to track the number of vehicles created
# 4.Demonstrate single inheritance and multilevel inheritance with appropriate classes

class Vehicle:
    #class variable
    vehicle_count=0
    def __init__(self):
        Vehicle.vehicle_count +=1
    #method
    def start(self):
        print("Vehicle Started")
#Derived class-->single inheritence
class Car(Vehicle):
    def drive(self):
        print("Car Drive")

class Petrol(Car):
    def Petrol_filling(self):
        print("Petrol_filling")
#object creation
v=Vehicle()
c=Car()
p=Petrol()

#method call
v.start()
c.start()
c.drive()
p.start()
p.drive()
p.Petrol_filling()
print(Vehicle.vehicle_count)