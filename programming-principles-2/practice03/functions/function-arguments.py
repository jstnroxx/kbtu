# Data can be passed into the function as arguments to use it further, we do that by adding them into the function parentheses
def greetSomeone(name):
    print("Hello!", name)
    
# We can add as many arguments as we want, just separate them with a comma
def greetThreePeople(name1, person2, thirdGuy):
    print(f"Hello! {name1}, {person2} and {thirdGuy}")
    
# Argument is a value that we pass into the function upon calling it, whereas parameter is a variable specified in function declaration inside the parentheses
def myFunction1(name): # "name" is a parameter
    print("Hello", name)

myFunction1("Maxim") # "Maxim" is an argument

# By default, a function MUST be called with the correct number of arguments or else we will get an error
def myFunction2(fname, lname):
    print(fname + " " + lname)

myFunction2("Maxim", "Smirnov")

# We can assign default values to the parameters, so if the function will be called without arguments, it will use the value provided as default
def greet(name = "friend"):
    print("Hello!", name)
    
greet()    

def myFunction3(country = "Norway"):
    print("I am from", country)

myFunction3("Sweden")
myFunction3("India")
myFunction3()
myFunction3("Brazil")

# We can send arguments with the "key = value" syntax, so the order of the arguments wont matter
def myPet(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

myPet(name = "Car", animal = "cat")

# When we call a function with arguments without using keywords, they are called positional arguments, positional arguments MUST be in the correct order
def myPet(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

myPet("cat", "Avtobus")

# We can mix positional and keyword arguments in a function call, however, positional arguments MUST come before keyword arguments
def myPet2(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

myPet2("cat", name = "(insert_a_cat_name_here)", age = 5)

# We can send any datatype as an argument to a function (e.g. string, list, dictionary, etc.), the datatype will be preserved inside of the function
def showcaseMyFruits(fruitList):
    for fruit in fruitList:
        print(fruit)
        
myFruits = ["apple", "banana", "fruit3"]
showcaseMyFruits(myFruits)

# We can specify the function to accept ONLY positional arguments, to do that add ", /" after the arguments
def greetBro(bro, /):
    print("Whatsapp", bro)
    
greetBro("dude")

# To specify that a function can accept only keyword arguments, simply add "* ," before the arguments
def greetBro(*, bro):
    print("Whatsapp", bro)
    
greetBro(bro = "dude")

# We can combine both argument types in the same function, arguments before "/" are positional-only, and arguments after "*" are keyword-only
def mySum(a, b, /, *, c, d):
  return a + b + c + d

result = mySum(5, 10, c = 15, d = 20)
print(result)




