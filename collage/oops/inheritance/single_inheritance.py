class a:
    def one(self):
        print("this is parent")

class b(a):
    def two(self):
        print("this is child")

obj=b()
obj.one()
obj.two()