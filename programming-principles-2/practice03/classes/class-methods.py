# Method is a function declared for a specific class inside of it. The "self" parameter is a reference to the current instance of the class
class Person:
    def greet(self):
        print("Hello, I am a person!")

p1 = Person()
p1.greet()
# (The "self" parameter must be the first parameter of any method in the class, the "self" parameter links the method to the specific object)

# Methods (e.g. greet()) can access and modify object properties using "self"
class Person2:
    def __init__(self, _name):
        self.name = _name
    
    def greet(self):
        print("Hello, I am a person, and my name is", self.name)

p2 = Person2("Maxim")
p2.greet()

class Person3:
    def __init__(self, _name, _age = 19):
        self.name = _name
        self.age = _age
    
    def greet(self):
        print("Hello, I am a person, and my name is", self.name)
        
    def getOld(self):
        self.age = 70
        print(self.name, f"is old now. (Age: {self.age})")

p2 = Person3("Maxim")
p2.getOld()

# We can also delete a method from a class
del Person3.getOld

# We can also specify the "__str__()" method which is a special method that controls what is returned when the object is printed
class Person4:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p4 = Person4("Maxim", 19)
print(p4)
