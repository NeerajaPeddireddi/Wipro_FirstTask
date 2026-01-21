from abc import ABC, abstractmethod
import json
import csv
import time

# DECORATORS
def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__} executed successfully")
        return result
    return wrapper

def admin_only(func):
    def wrapper(*args, **kwargs):
        is_admin =True
        if not kwargs.get("is_admin", False):
            raise PermissionError("Access Denied: Admin privileges required")
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[TIME] {func.__name__} took {time.time()-start:.4f}s")
        return result
    return wrapper

# DESCRIPTORS
class MarksDescriptor:
    def __set__(self, instance, value):
        if len(value) != 5 or not all(0 <= m <= 100 for m in value):
            raise ValueError("Marks should be 5 subjects between 0 and 100")
        instance.__marks = value

    def __get__(self, instance, owner):
        return instance.__marks

class SalaryDescriptor:
    def __get__(self, instance, owner):
        if getattr(instance, "is_admin", False):
            return instance.__salary
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, instance, value):
        instance.__salary = value

#ABSTRACT CLASS
class Person(ABC):
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass
    #Destructor
    def __del__(self):
        print(f"[CLEANUP] {self.name} object deleted")

# DEPARTMENT -->Simple helper class
class Department:
    def __init__(self, name):
        self.name = name

# STUDENT
class Student(Person):
    marks = MarksDescriptor() #Used to validate the marks

    def __init__(self, pid, name, department, semester, marks):
        super().__init__(pid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def get_details(self):
        print("\nStudent Details")
        print("----------------")
        print("Name      :", self.name)
        print("Role      : Student")
        print("Department:", self.department)

    def average(self):
        return sum(self.marks) / len(self.marks)

    @timer
    @logger
    def calculate_performance(self):
        avg = round(self.average(), 2)
        grade = "A" if avg >= 90 else "B" if avg >= 80 else "C"
        return avg, grade

    def enroll(self, course):
        self.courses.append(course)
    #operator overloading
    def __gt__(self, other):
        return self.average() > other.average()

# ---------------- FACULTY ----------------
class Faculty(Person):
    salary = SalaryDescriptor()#validate the salary

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        print("\nFaculty Details")
        print("----------------")
        print("Name      :", self.name)
        print("Role      : Faculty")
        print("Department:", self.department)

# COURSE
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty
    def get_details(self):
        print("\nCourse Details")
        print("----------------")
        print("Code      :", self.code)
        print("Name      :", self.name)
        print("Credits   :",self.credits)
        print("Faculty:", self.faculty)
    def __add__(self, other):
        return self.credits + other.credits

# ITERATOR
class CourseIterator:
    def __init__(self, courses):
        self.courses = courses
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.courses):
            course = self.courses[self.index]
            self.index += 1
            return course.name
        raise StopIteration

# GENERATOR
def student_generator(students):
    print("\nFetching Student Records...")
    for s in students:
        yield f"{s.pid} - {s.name}"

# FILE HANDLING
@admin_only
def save_students_json(students,**kwargs):
    data = [{
        "id": s.pid,
        "name": s.name,
        "department": s.department,
        "semester": s.semester,
        "marks": s.marks
    } for s in students]

    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Student data successfully saved to students.json")

@admin_only
def generate_students_csv(students,**kwargs):
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
        for s in students:
            avg, grade = s.calculate_performance()
            writer.writerow([s.pid, s.name, s.department, avg, grade])
    print("CSV Report generated successfully")

# MAIN PROGRAM
students = []
faculty_list = []
courses = []

while True:
    print("\nSMART UNIVERSITY MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. Add Faculty")
    print("3. Add Course")
    print("4. Enroll Student to Course")
    print("5. Calculate Student Performance")
    print("6.Student and Faculty Details(Polymorphism)")
    print("7. Compare Two Students")
    print("8.Descriptor Validation Output")
    print("9.Decorator Output (Logging / Access Control)")
    print("10.Iterator / Generator Output")
    print("11.File Output")
    print("12.Exception Handling Output")
    print("13. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            pid = input("Student ID: ")
            if any(s.pid == pid for s in students):
                raise ValueError("Student ID already exists")
            s = Student(
                pid,
                input("Name: "),
                input("Department: "),
                int(input("Semester: ")),
                list(map(int, input("5 Marks: ").split()))
            )
            students.append(s)
            print("Student Created Successfully")
            s.get_details()

        elif choice == "2":
            f = Faculty(
                input("Faculty ID: "),
                input("Name: "),
                input("Department: "),
                int(input("Salary: "))
            )
            f.is_admin = True
            faculty_list.append(f)
            print("Faculty Created Successfully")
            f.get_details()

        elif choice == "3":
            c = Course(
                input("Course Code: "),
                input("Course Name: "),
                int(input("Credits: ")),
                faculty_list[0].name if faculty_list else "Not Assigned"
            )
            courses.append(c)
            print("Course Added Successfully")
            c.get_details()

        elif choice == "4":
            student = students[0]
            course = courses[0]
            student.enroll(course)
            print("\nEnrollment Successful")
            print("--------------------------------")
            print("Student Name :", student.name)
            print("Course       :", course.name)

        elif choice == "5":
            student = students[0]
            avg, grade = students[0].calculate_performance()
            print("\nStudent Performance Report")
            print("--------------------------------")
            print("Student Name :", student.name)
            print("Marks        :", student.marks)
            print("Average      :", avg)
            print("Grade        :", grade)
        elif choice == "6":
            if students and faculty_list:

                for s in students:
                    s.get_details()

                for f in faculty_list:
                    f.get_details()
            else:
                print("Add at least one student and one faculty first.")
        elif choice == "7":
            if len(students) >= 2:
                print("Compare Two Students (> operator)")
                print("Comparing Students Performance")
                print("--------------------------------")
                print(f"{students[0].name} > {students[1].name} : {students[0] > students[1]}")
            else:
                print("Add at least 2 students to compare.")

            if len(courses) >= 2:
                total_credits = courses[0] + courses[1]
                print("\nMerge Course Credits (+ operator)")
                print("Total Credits After Merge :", total_credits)
            else:
                print("Add at least 2 courses to merge credits.")
        elif choice == "8":
            try:
                students[0].marks = [101, 50, 60, 70, 80]  # invalid marks
            except Exception as e:
                print("Invalid Marks")
                print("Error:", e)

            try:
                print(faculty_list[0].salary)  # accessing salary directly
            except Exception as e:
                print("Unauthorized Salary Access")
                print(e)
        elif choice == "9":
            # Call a method decorated with logger
            students[0].calculate_performance()

            # Call a method decorated with admin_only
            try:
                save_students_json(students,is_admin=True)
            except Exception as e:
                print(e)
        elif choice == "10":
            print("Student Record Generator")
            print("Fetching Student Records...")
            print("--------------------------------")
            for rec in student_generator(students):
                print(rec)
            print("\nCourse Iterator Output")
            print("--------------------------------")
            course_iter = CourseIterator(courses)
            for cname in course_iter:
                print(cname)

        elif choice == "11":
            save_students_json(students,is_admin=True)
            generate_students_csv(students,is_admin=True)

        elif choice == "12":
            print("\nException Handling Output")
            print("--------------------------------")
            # 1️⃣ Duplicate Student ID
            try:
                dup_id = "101"  # Example ID already used
                if any(s.pid == dup_id for s in students):
                    raise ValueError(f"Student ID '{dup_id}' already exists")
                # If not exists, this won't run, but in this example it will
                s = Student(dup_id, "Duplicate Student", "CSE", 4, [50, 50, 50, 50, 50])
                students.append(s)
            except Exception as e:
                print("Error:", e)

            # 2️⃣ Non-existent file access
            try:
                with open("nofile.json") as f:  # intentionally wrong file
                    pass
            except Exception as e:
                print("Error:", e)

        elif choice == "13":
            print("Thank you for using Smart University Management System")
            break
        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)
