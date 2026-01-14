from functools import reduce
#1. Uses range() to generate numbers from 1 to 20
for i in range(1,21):
    print(i)

#2. Uses filter() with a lambda to select only even numbers
numbers=range(1,21)
evennums=list(filter(lambda x:x%2==0,numbers))
print(evennums)

#3. Uses map() with a lambda to square the filtered numbers
sqnum=list(map(lambda x:x**2,evennums))
print(sqnum)
#4. Uses reduce() to calculate the sum of squared even numbers
sumsqnum=reduce(lambda x,y:x+y,sqnum)
print(sumsqnum)
#5. Uses enumerate() to print the index and value of the final result li
fruits=["apple","banana","mango"]
for i,fruit in enumerate(fruits):
    print(i,fruit)