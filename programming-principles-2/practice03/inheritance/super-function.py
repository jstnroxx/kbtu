class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("Inited person.")

    def printname(self):
        print(self.firstname, self.lastname)

# Inheritance features a "super()" function that will make the child class inherit all the methods and properties from its parent
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
# (By using the "super()" function, you do not have to use the name of the parent element and provide "self", it will automatically inherit the methods and properties from its parent)

# We can add additional exclusive for the child properties to initialize by simply putting them inside the outer "__init__()" and then assigning them to "self"
class Student2(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age