class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def diaplay(self):
        print("name : ",self.name)
        print("age: ",self.age)

s1=student('syam',20)
s1.diaplay()