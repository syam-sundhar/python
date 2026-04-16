#1 Write a Python program to add two numbers using lambda function.
a=int(input("Enter the number: "))
b=int(input("Enter the another number: "))
add=lambda x,y:x+y
print("The sum of two numbers is: ",add(a,b))
print("--------------------------------------------------------------")
#2. Write a lambda function to find the square of a number.
num=int(input("Enter the number: "))
square=lambda x:x**2
print("the square of the number is: ",square(num))
print("--------------------------------------------------------------")
# 3. Write a lambda function to find the cube of a number.
num=int(input("enter the number: "))
cube=lambda x:x**3
print("the cube of the number is: ",cube(num))
print("--------------------------------------------------------------")
#4.	Write a lambda function to check whether a number is even or odd.
num=int(input("Enter the number: "))
check=lambda x:"even" if x%2==0 else "odd"
print("the number is: ",check(num))
print("--------------------------------------------------------------")
#5.	Write a lambda function to find the maximum of two numbers.
a=int(input("Enter the number: "))
b=int(input("Enter the another number: "))
check=lambda x,y:x if x>y else y
print("the maximum of two numbers is: ",check(a,b))
print("--------------------------------------------------------------")
# 6.Use lambda with map() to add 5 to each element in a list.
nums=[1,2,3,4,5]
add_five=map(lambda x:x+5,nums)
print(list(add_five))
print("--------------------------------------------------------------")
#7.	Use lambda with map() to multiply corresponding elements of two lists.
nums1=[1,2,3,4,5]
nums2=[6,7,8,9,10]
mul_two=list(map(lambda x,y:x*y,nums1,nums2))
print(mul_two)
print("--------------------------------------------------------------")
#8.	Use lambda with filter() to extract even numbers from a list.
nums=[1,2,3,4,5,6,7,8,9,10]
even_nums=list(filter(lambda x:x%2==0,nums))
print("the even numbers are: ",even_nums)
print("--------------------------------------------------------------")
#9.	Use lambda with filter() to extract odd numbers from a list.
odd_nums=list(filter(lambda x:x%2!=0,nums))
print("the odd numbers are: ",odd_nums)
print("--------------------------------------------------------------")
#10.	Use lambda with reduce() to find the minimum element in a list.
from functools import reduce
min_num=reduce(lambda x,y:x if x>y else y,nums) # how it works: it compares the first two elements of the list and returns the smaller one, then it compares that result with the next element in the list and so on until it finds the minimum element.
print("the minimum number is: ",min_num)
print("--------------------------------------------------------------")
#11.	Use lambda with reduce() to concatenate a list of strings.
list_str=["Hello","World","Python","Programming"]
concat_str=reduce(lambda x,y:x+y,list_str)
print("the concatenated string is: ",concat_str)
print("--------------------------------------------------------------")
#12.Sort numbers in descending order using lambda
nums=[1,2,3,4,5,6,7,8,9,10]
nums_sorted=sorted(nums,reverse=True)
print("the numbers sorted in descending order are: ",nums_sorted)
print("--------------------------------------------------------------")
#13.Use lambda to reverse each string in a list.
list_str=["Hello","World","Python","Programming"]
reversed_str=list(map(lambda x:x[::-1], list_str))
print(reversed_str)