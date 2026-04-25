class ValueToosmaller:
    def __init__(self):
        
        """value is too smaller you are taking"""
class ValueTooLarger:
    def __init__(self):
        """value is too larger you are taking"""
number=10
while True:
    try:
        i_num =int(input("Enter a number:"))
        if i_num<number:
            raise ValueToosmaller
        elif i_num>number:
            raise ValueTooLarger
        break
    except ValueToosmaller:
        print("this value is too small,try again!")
print("congrats you guess correct")