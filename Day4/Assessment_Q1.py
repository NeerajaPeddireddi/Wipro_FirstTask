# Question – Introduction to OOPs, Classes & Objects
# Topics: Introduction to OOPs, Understanding Classes & Objects
# Create a class Student that:
# 1.Has attributes name and roll_no
class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
obj=Student("Bharat",5)
print(obj.roll_no)
print(obj.name)

# 2.Has a method display_details()to print student information
class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display_details(self):
        print(self.name)
        print(self.roll_no)
obj=Student("Bharat",5)
obj.display_details()

# 3. Create at least two objects of the class and display their details
class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display_details(self):
        print(self.name)
        print(self.roll_no)
obj1=Student("Bharat",5)
obj2=Student("Sathwik",4)
obj1.display_details()
obj2.display_details()
