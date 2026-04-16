age=input('enter your age: ')
if age.isdigit():
    age=int(age)
    print("type validation done")
else:
    print("type validation incomplete")
print("-"*25)
n=int(input('enter a number: '))
if 1<n<11:
    print("range validation done")
else:
    print("range validation incomplete")
print("-"*25)
p=input('enter password: ')
if len(p)>=6:
    print('strong')
else:
    print("week")
print("-"*25)
email=input("enter email: ")
if '@' in email and '.' in email:
    print("valid mail")
else:
    print("invalid mail")
print("-"*25)
