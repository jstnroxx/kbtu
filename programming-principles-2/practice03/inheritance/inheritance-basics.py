# Inheritance allows us to define a class that inherits all the methods and properties from another class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("Inited person.")

    def printname(self):
        print(self.firstname, self.lastname)

# Use the "Person" class to create an object, and then execute the "printname" method
x = Person("John", "Doe")
x.printname()

# Create a class named "Student", which will inherit the properties and methods from the "Person" class by specifying it in parentheses after the child class name
class Student(Person):
    pass
# (Use pass if we don't want to implement anything extra to the child class)

x = Student("Maxim", "Smirnov")
x.printname()
# (What we got at the moment is an exact clone of a "Person" class but with a different name)

# When we add the "__init__()" function, the child class will no longer inherit the parent's "__init__()" function
class Student2(Person):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
x = Student2("Maxim2", "Smirnov2")
        
# To keep the inheritance of the parent's "__init__()" function, add a call to the parent's "__init__()" function
class Student3(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
x = Student3("Maxim3", "Smirnov3")