# Properties (i.e. variables) defined outside methods belong to the class itself (class properties) and are shared by all objects
class Person:
    species = "Human" # Class property

    def __init__(self, name):
        self.name = name # Instance property

p1 = Person("Maxim")
p2 = Person("Gosha")

print(p1.name, p1.species)
print(p2.name, p2.species)

# When you modify a class property, it affects all objects
Person.species = "Homo sapiens"
print(p1.name, p1.species)
print(p2.name, p2.species)

# We can delete instance properties, HOWEVER we cannot delete class properties by using "del" on any object
del p1.name