nums=[1,2,3,4,5]
#map function is used to apply a function to all the items in an iterable and return a list of the results.
print(list(map(lambda x:x**2,nums)))
#filter function is used to filter the items in an iterable based on a function that returns a boolean value.
print(list(filter(lambda x:x%2==0,nums)))
#reduce function is used to apply a function of two arguments cumulatively to the items of an iterable from left to right, reducing the iterable to a single value.
from functools import reduce
l=[1,2,3,4]
print(reduce(lambda x,y:x+y,l))