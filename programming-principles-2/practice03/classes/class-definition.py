# Class is some kind of a template to create multiple independent objects with the same structure, variables, and specific methods
# We create a class named by using the keyword "class", in our case with a property named x
class MyClass:
    x = 100
    
# Now we can use the class named "MyClass" to create objects
obj1 = MyClass()

# We access or modify methods and variables inside of an object by using the dot notation
print(obj1.x)

# We can also add a new property to an object this way
obj1.y = 999
print(obj1.y)

# You can delete objects by using the "del" keyword
del obj1

# We can create any amount of objects from the same class
obj1 = MyClass()
obj2 = MyClass()
objETC = MyClass()
print(obj1.x, obj2.x, objETC.x)

# Each object is independent and has its own copy of the class properties
obj2.x = 228
print(obj1.x, obj2.x, objETC.x)

# We can also use "pass" for classes to declare them without any contents
class ImplementLater:
    pass

# Deleting a modified property of an object will reset it to a default provided in class, will completely delete if property not explicitly defined in class declaration (as "x" in "MyClass")
del obj2.x
print(obj1.x, obj2.x, objETC.x)

# Deleting a property of a class will remove it for all its objects
del MyClass.x
try:
    print(obj1.x)
except:
    print("Failed")
    

    
