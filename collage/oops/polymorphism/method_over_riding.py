class mother:
    def parent(self):
        print("this is base class")
class child(mother):
    def parent(self):
        super().parent()
        print("this is child class")
ch = child()
ch.parent()