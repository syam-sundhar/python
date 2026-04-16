num=list(range(0,41,10))
print(num)
total=0
for i in num:
    total+=i
    print('running total: ',total)
print("_"*25)
n=int(input("enter how many numbers: "))
total=0
for i in range(n):
    num=int(input("enter number: "))
    total+=num
print('total:',total)
