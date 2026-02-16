import math
import time
from multiprocessing import Pool,cpu_count

numbers = [50000, 60000, 55000, 45000, 70000]

def calculate_fact(n):
    return math.factorial(n)
start_time = time.time()
sequential_fact = []
for num in numbers:
    sequential_fact.append(calculate_fact(num))
    print("fact calculated")

end_time=time.time()
print(end_time-start_time)

if __name__=="__main__":
    mul_start_time = time.time()
    with Pool(cpu_count()) as pool:
        result=pool.map(calculate_fact, numbers)
    for num in numbers:
        print("fact calculated")
    mul_end_time=time.time()
    print(mul_end_time-mul_start_time)