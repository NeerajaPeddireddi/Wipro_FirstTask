from abc import ABC,abstractmethod
import json
import csv

#Decorators
def logger(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        print(f"[LOG] Method {func.__name__} executed successfully")
        return result
    return wrapper
#Descriptors
class MarksDescriptor:
    def __get__(self, instance, owner):
        return instance.__marks
    def __set__(self, instance, value):
        if all(0<m<=100 for m in value):
            instance.__marks = value
        else:
            raise ValueError("Marks should be between 0 and 100")
#Abstract class
class Person(ABC):
    def __init__(self,pid,name,department):
        self.pid = pid
        self.name = name
        self.department = department
    @abstractmethod
    def get_details(self):
        pass
#Student class
class Student(Person):
    marks = MarksDescriptor()
    def __init__(self,pid,name,department,semester,marks):
        super().__init__(pid,name,department)
        self.semester = semester
        self.marks = marks
    def get_student_details(self):
        print("\nStudent Details")
        print("----------------")
        print("Name      :", self.name)
        print("Role      : Student")
        print("Department:", self.department)
    def average(self):
        return round(self.marks.average(),2)
    @logger
    def calculate_performance(self):
        avg = self.average()
        if avg>=90:
            grade = "A"
        elif avg>=80:
            grade = "B"
        else:
            grade = "C"
        return avg,grade
    def __gt__(self,other):
        return self.average() > other.average()
#Faculty class
class Faculty(Person):
    def __init__(self,fid,name,department,salary):
        super().__init__(fid,name,department)
        self.salary = salary
    def get_faculty_details(self):
        print("\nFaculty Details")
        print("----------------")
        print("Name      :", self.name)
        print("Department:", self.department)
        print("Salary:     ", self.salary)
#Course class
class Course(Person):
    def __init__(self,code,name,credits,faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty
    def __add__(self,other):
        return self.credits + other.credits
#Generator
def student_generator(students):
    print("\nFetching Student Records...")
    for s in students:
        yield f"{s.pid} - {s.name}"
#File handling
def save_students_json(students):
    data=[]
    for s in students:
        data.append({
            "id":s.pid,
            "name":s.name,
            "department":s.department,
            "semester":s.semester,
            "marks":s.marks,
        })
    with open("students.json",'w') as f:
        json.dump(data,f,indent=4)
    print("Student data successfully saved to students.json")

def generate_students_csv(students):
    with open("students.csv",'w',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Id","Name","Department","Average","Grade"])
        for s in students:
            avg,grade=s.calculate_performance()
            writer.writerow([s.id,s.name,s.department,avg,grade])
    print("CSV Report generated successfully")
students=[]
faculty_list=[]
courses=[]
while True:
    print("\nSMART UNIVERSITY MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. Add Faculty")
    print("3. Add Course")
    print("4. Calculate Student Performance")
    print("5. Compare Two Students")
    print("6. Generate Reports")
    print("7. Display Students (Generator)")
    print("8. Exit")
    choice=input("Enter your choice:")
    try:
        if choice=="1":
            pid=input("Student Id:")
            name=input("Student Name:")
            dept=input("Student Department:")
            sem=input("Student Semester:")
            marks=list(map(int,input("Student 5 Marks:").split()))
            s=Student(pid,name,dept,sem,marks)
            students.append(s)
            print("Student Created Successfully")
            s.get_student_details()
        elif choice=="2":
            fid=input("Faculty Id:")
            name=input("Faculty Name:")
            dept=input("Faculty Department:")
            salary=int(input("Faculty Salary:"))

            f=Faculty(fid,name,dept,salary)
            faculty_list.append(f)
            print("Faculty Created Successfully")
            f.get_faculty_details()
        elif choice=="3":
            code=input("Course Code:")
            cname=input("Course Name:")
            credits=int(input("Course Credits"))
            fname=faculty_list[0].name if faculty_list else "Not Assigned"

            c=Course(code,cname,credits,fname)
            courses.append(c)
            print("Course Created Successfully")
        elif choice == "4":
            s = students[0]
            avg, grade = s.calculate_performance()
            print("\nAverage:", avg)
            print("Grade:", grade)

        elif choice == "5":
            if len(students) >= 2:
                print(students[0].name, ">", students[1].name, ":", students[0] > students[1])

        elif choice=="5":
            if len(students)>=2:
                print(students[0].name,">",students[1].name, ":", students[0] > students[1])

        elif choice == "6":
            save_students_json(students)
            generate_students_csv(students)

        elif choice == "7":
            for rec in student_generator(students):
                print(rec)

        elif choice == "8":
            print("Thank you for using Smart University Management System")
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)