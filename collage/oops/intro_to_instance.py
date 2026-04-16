class numdisplay :
    def __init__ (self):
        self.x = 100
    def display (self):
        global y
        y=10
        print("instance variable is ",self.x)
        print("normal variable is ",y)
n = numdisplay()
n.display()
print("outside instance variable is ",n.x)
print(y)