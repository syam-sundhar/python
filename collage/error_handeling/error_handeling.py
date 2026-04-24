#-------------------
try:
    marks=25
    result=25/0
    print(result)
except ZeroDivisionError:
    print("A number can't divisible by Zero")
#-------------------
try:
    list1=[1,2,3]
    print(list1[8])
except IndexError:
    print("index is not found")
#-------------------
try:
    file=open("file.txt","r")
    print(file.read())
except FileNotFoundError:
    print("file is not found")
finally:
    print("code completed")
#-------------------
