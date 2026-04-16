class father:
    def one(self):
        print("this is father")

class mother:
    def two(self):
        print("this is mother")

class c(father,mother):
    def three(self):
        print("this is son")

obj=c()
obj.one()
obj.two()
obj.three()