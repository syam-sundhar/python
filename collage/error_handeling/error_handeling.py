#zero division error
try:
    marks=25
    result=25/0
    print(result)
except ZeroDivisionError:
    print("A number can't divisible by Zero")
print("-------------------------")
#index error
try:
    list1=[1,2,3]
    print(list1[8])
except IndexError:
    print("index is not found")
print("-------------------------")
#file not found error
try:
    file=open("file.txt","r")
    print(file.read())
except FileNotFoundError:
    print("file is not found")
finally:
    print("code completed")
print("-------------------------")
#Asserection error
try:
    age=10
    assert age>=18
except AssertionError:
    print("age must grater then 18")
print("-------------------------")
#name error
try:
    value=10
    print(Value)
except NameError:
    print("variable not found")
print("-------------------------")
#type error
try:
    a=10
    b="syam"
    print(a+b)
except TypeError:
    print("operation is not valid")
print("-------------------------")
#import error
try:
    import syam
    a=10
except ImportError:
    print("import is not done!")
print("-------------------------")
#key error
try:
    a={
        "a":1,
        "b":2
    }
    print(a["c"])
except KeyError:
    print("key is not found")