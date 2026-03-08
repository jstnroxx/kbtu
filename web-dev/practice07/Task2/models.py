class Animal:
    def __init__(self, _name, _age, _color, _type = "animal"):
        self.name = _name
        self.age = _age
        self.color = _color
        self.type = _type

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.color} {self.type}."

    def speak(self):
        print(f"{self.name} speaks!")
        
    def sleep(self):
        print(f"{self.name} has gone to sleep.")
        
class Dog(Animal):
    def __init__(self, _name, _age, _color):
        super().__init__(_name, _age, _color, "dog")
        
    def speak(self):
        print(f"{self.name} barks!")
        
    def chaseCats(self):
        print(f"{self.name} went after some cats.")
        
class Cat(Animal):
    def __init__(self, _name, _age, _color, _indoor = True):
        super().__init__(_name, _age, _color, "cat")
        self.isIndoor = _indoor
        
    def speak(self):
        print(f"{self.name} meows!")
        
    def stealFood(self):
        print(f"{self.name} has stolen some food off the table.")
        