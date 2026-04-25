try:
    file=open("student.txt","r")
except:
    print("file not found")
finally:
    print("code completd")
