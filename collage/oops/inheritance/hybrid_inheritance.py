class animal:
    def sound(self):
        print("animal make sound")

class mammal(animal):
    def make_sound(self):
        print("mammal make sound")

class birds:
    def do_sound(self):
        print("birds make sound")

class bat(mammal,birds):
    pass

obj=bat()
obj.do_sound()
obj.make_sound()
obj.sound()