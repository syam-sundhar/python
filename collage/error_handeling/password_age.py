class PasswordLenghtERROR(Exception):
    pass
class AgeError(Exception):
    pass
class ageandpasswordlenerror(Exception):
    pass
while True:
    try:
        password=input("enter your password: ")
        age=int(input("enter your age: "))
        if len(password)<=8 and age<=18:
            raise ageandpasswordlenerror
        elif age<=18:
            raise AgeError
        elif len(password)<=8:
            raise PasswordLenghtERROR
        break
    except ageandpasswordlenerror:
        print("password is too small and age must be grater than 18!")
    except PasswordLenghtERROR:
        print("password is too small")
    except AgeError:
        print("Age must be grater than 18!")
print("your account is created🎉")