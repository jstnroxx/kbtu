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