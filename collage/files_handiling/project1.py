f=open("project1.txt","a")
name=input("enter your name: ")
name="name:"+name+"\n"
f.write(name)
age=int(input("enter your age: "))
age="age :"+str(age)+"\n"
f.write(age)
f.close()