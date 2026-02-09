class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("Inited person.")

    def printname(self):
        print(self.firstname, self.lastname)

# If we add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden
class Student(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age
        
    def printname(self):
        print("Student:", self.firstname, self.lastname)
        
s1 = Student("Maxim", "Smirnov", 19)
s1.printname()