class FirstParent:
    def __init__(self, _x):
        self.x = _x
        print("Initialized first parent.")
        
    def showX(self):
        print(self.x)
        
    def printFirst(self):
        print("Print from a first parent.")
        
class SecondParent:
    def __init__(self, _y):
        self.y = _y
        print("Initialized second parent.")
        
    def showY(self):
        print(self.y)
        
    def printSecond(self):
        print("Print from a second parent.")

# A child class can inherit attributes and methods from more than one parent class

# To use multiple inheritance, list the parent classes in the definition of the child class, separated by commas
class Child(FirstParent, SecondParent):
    def __init__(self, _x, _y):
        FirstParent.__init__(self, _x)
        SecondParent.__init__(self, _y)
        
c1 = Child(5, 8)
c1.showX()
c1.showY()
c1.printFirst()
c1.printSecond()

# An abstract base class (ABC) is a blueprint for other classes that defines a common interface and forces subclasses to implement specific methods
# In order to use it, we have to import the following
from abc import ABC, abstractmethod

# To create an abstract base class we set a parent of a class to "ABC"
class Vehicle(ABC):
    
    #"@abstractmethod" before a method declaration forces all subclasses to override the following method
    @abstractmethod
    def startEngine(self):
        pass
    
    # The following is a "concrete method" which provides this functionality to every subclass
    def identifyItem(self):
        print("It is a vehicle.")
        
class Motorcycle(Vehicle):
    def startEngine(self):
        print("Kickstarted the engine.")

m1 = Motorcycle()
m1.identifyItem()