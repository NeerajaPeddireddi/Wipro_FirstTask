# 1.
# NumPy / Pandas(Data Manipulation)
# Question:You have a dataset of student scores in a class as a Python list of dictionaries:
#     students = [
#         {"name": "Alice", "score": 85},
#         {"name": "Bob", "score": 92},
#         {"name": "Charlie", "score": 78},
#         {"name": "David", "score": 90},
#         {"name": "Eva", "score": 88}
#     ]
#
# Convert this data into a Pandas DataFrame.
# Using NumPy, calculate the mean, median, and standard deviation of the students' scores.
# Add a new column to the DataFrame called "above_average" which is True if the student's score is above the mean and False otherwise.

import numpy as np
import pandas as pd
students = [
{"name": "Alice", "score": 85},
{"name": "Bob", "score": 92},
{"name": "Charlie", "score": 78},
{"name": "David", "score": 90},
{"name": "Eva", "score": 88}
]

df=pd.DataFrame(students)
mean_score=np.mean(df["score"])
median_score=np.median(df["score"])
std_score=np.std(df["score"])
df["above_average"]=df["score"]>mean_score
print("Mean:",mean_score)
print("Median",median_score)
print("Standard Deviation:",std_score)
print(df)