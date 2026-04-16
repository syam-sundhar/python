class a:
    def one(self):
        print("this is grandparent")

class b(a):
    def two(self):
        print("this is parentr")

class c(b):
    def three(self):
        print("this is son")

obj=c()

obj.one()
obj.two()
obj.three()