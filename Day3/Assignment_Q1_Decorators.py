# Question – Decorators
# Topic: Decorators
# Write a decorator called @execution_time that:
# 1. Measures the execution time of a function
# 2. Prints the function name and execution time
# 3. Apply this decorator to a function that calculates the factorial of a number using recursion
import time
def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function:'{func.__name__}' executed in  ", end - start,"seconds")
        return result
    return wrapper
@execution_time
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
n=int(input("Enter the number:"))
res=factorial(n)
print(f"Factorial of {n} is {res}")

