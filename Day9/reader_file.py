import json
from D9_Practice import writer_fun
def reader_fun(filename):
    with open(filename,"r") as file:
        print(file.read())
        print("File read successfully")
writer_fun("data.txt")
reader_fun("data.txt")
