def int_palindrom(num):
    temp=num
    rev=0
    while temp>0:
        digit=temp%0
        rev=rev*10+digit
        temp=temp//10
    return rev
def str_palindron(word):
    rev=word.rev()
    
