# Question – Iterators and Generators
# Topic: Iterators & Generators
# 1. Create a custom iterator class that iterates over numbers from 1 to N
# Using Iterator
class NumberIterator:
    def __init__(self,number):
        self.number=number
        self.curreent=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.curreent<=self.number:
            val=self.curreent
            self.curreent+=1
            return val
        else:
            raise StopIteration
obj=NumberIterator(10)

for i in obj:
    print(i)
# Using Generator
class NumIterator:
    def __init__(self,number):
        self.number=number
    def __iter__(self):
        for i in range(1,self.number+1):
            yield i
obj=NumIterator(10)
it=iter(obj)
print(next(it))

# 2. Create a generator function that yields the first N Fibonacci numbers
def fib(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
it=iter(fib(10))
print(next(it))
print(next(it))

# Using For Loop
def fib(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
for i in fib(10):
    print(i)

# 3. Demonstrate the difference between using the iterator and generator by printing values using a for loop
# Using Iterator
class EvenIterator:
    def __init__(self,n):
        self.n=n
        self.current=2
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.n:
            val=self.current
            self.current+=2
            return val
        else:
            raise StopIteration
print("Even numbers using Iterator:")
for i in EvenIterator(10):
    print(i)

# Generator
def evengenerator(number):
    for i in range(number):
        if i%2==0:
            yield i
for i in evengenerator(11):
    print(i)
