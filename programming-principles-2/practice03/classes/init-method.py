# The "__init__()" method is used to assign values to individual object properties, or to perform operations that are necessary when the object is being created
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Object {self} successfully initialized with name: {self.name} and age: {self.age}!\n")

p1 = Person("Maxim", 19)

print(p1.name, p1.age)
# (The "__init__()" method is called automatically every time the class is being used to create a new object)

# We can also set default values for parameters in the "__init__()" method
class Person2:
    def __init__(self, name, age = 19):
        self.name = name
        self.age = age

p2 = Person2("Maxim")

print(p2.name, p2.age)

# The "__init__()" method can have as many parameters as you need
class Person3:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p3 = Person3("Maxim", 19, "Almaty", "Kazakhstan")

print(p3.name, p3.age, p3.city, p3.country)