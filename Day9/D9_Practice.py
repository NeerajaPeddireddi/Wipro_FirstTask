# Revised all the topics discussed from past 8 days
import json
def writer_fun(filename):
    with open(filename,"w") as f:
        for i in range (1,11):
            f.write(str(i)+"\n")
        print("File written successfully")

