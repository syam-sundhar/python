class ValueTooSmallError(Exception):
    """value is too smaller you are taking"""
class ValueTooLargeError(Exception):
    """value is too larger you are taking"""
    pass
number=10
while True:
    try:
        i_num =int(input("Enter a number:"))
        if i_num<number:
            raise ValueTooSmallError
        elif i_num>number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("this value is too small,try again!")
    except ValueTooLargeError:
        print("this value is too larger,try again!")
print("congrats you guess correct")