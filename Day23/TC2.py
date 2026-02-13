import math,time
from multiprocessing import Pool,cpu_count
numbers = [50000, 60000, 55000, 45000, 70000]

def compute_factorial(n):
    return math.factorial(n)
if __name__ == "__main__":

    start_time = time.time()
    seq_res=[]
    for num in numbers:
        res = compute_factorial(num)
        seq_res.append(res)
        print(f"Sequential: Factorial of {num} calculated ")
    seq_time = time.time()-start_time
    print(f"\nSequential Time: {seq_time}")

    start_time1 = time.time()
    with Pool(cpu_count()) as p:
        parallel_res = p.map(compute_factorial, numbers)
    for num in numbers:
        print(f"Parallel: Factorial of {num} calculated")
    parallel_time = time.time()-start_time1
    print(f"\nParallel Time: {parallel_time}")