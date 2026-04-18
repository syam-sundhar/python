# reading whole
f=open("reading.txt","r")
print(f.read())
print(f.tell())
f.close()
print("-------------------")
# reading line
f=open("reading.txt","r")
print(f.readline())
print(f.readline())
f.close()
print("-------------------")
# reading lines 
f=open("reading.txt","r")
print(f.readlines())
f.close()