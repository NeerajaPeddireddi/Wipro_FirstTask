# Question – Functions, Modules, File Handling & Exceptions
# Topic: Functions, Modules (package), File Handling, Exceptions
# Create a small Python package with:
# 1.A module containing a function write_numbers_to_file(filename)
# 2. The function should write numbers 1–100 into a file
# 3. Handle possible exceptions such as:
# File not found
# Permission denied
# 4. Create another module that imports this function and reads the file content safely
from Write_num_file import write_numbers_to_file

def read_file(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found while reading")
    except PermissionError:
        print("Permission denied while reading")
    except Exception as e:
        print("Error:", e)

# Using the imported function
write_numbers_to_file("Assignment_File.txt")
read_file("Assignment_File.txt")
