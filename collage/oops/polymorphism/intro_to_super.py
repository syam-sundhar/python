class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent initialized: {self.name}")
    
    def greet(self):
        print(f"Hello from {self.name} (Parent)")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(f"Child initialized: Age {self.age}")

    def greet(self):
        super().greet()
        print(f"I am {self.age} years old.")

c = Child("Alex", 12)
c.greet()