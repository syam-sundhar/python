class display:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "student name is: " + self.name
d1=display('syam')
print(d1)