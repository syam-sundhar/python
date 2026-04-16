first=0
second=1
sum=0
n=int(input("enter the the number:"))
for i in range(0,n):
    print(sum)
    sum=first+second
    
    first=second
    second=sum
