num=int(input('enter a number: '))
n=len(str(num))
sum=0
temp=num
while temp>0:
    digt=temp%10
    sum=sum+(digt**n)
    temp=temp//10
if sum==num:
    print("amstrong")
else:
    print("not amstrong")
