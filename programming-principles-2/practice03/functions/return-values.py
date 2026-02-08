# Functions can return values by using the "return" statement 
def mySum(a, b):
    return a + b

sum = mySum(5, 8)
print(sum)

# Functions can return any data type, including lists, tuples, dictionaries, etc.
def getFruits():
  return ["cherry", "apple", "durian"]

myFruits = getFruits()
print(myFruits[0])
print(myFruits[1])
print(myFruits[2])
# (This one returned a list)

def myNumbers():
  return (52, 420)

x, y = myNumbers()
print("x:", x)
print("y:", y)
# (Whereas this one returned a tuple)

# Example that returns a dictionary with provided values
def createDict(val1, val2):
  return {"first" : val1, "second" : val2}

testDictionary = createDict(133, 7228)
print(testDictionary["first"])
print(testDictionary["second"])
