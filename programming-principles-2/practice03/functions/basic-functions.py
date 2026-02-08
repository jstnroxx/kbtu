# In python, a function is declared using "def" keyword
def myFunction():
    print("Some output from myFunction")
    
# To call a function, you basically need to write its name followed by parentheses
myFunction()

# We can call a function as many times as we need
myFunction()
myFunction()

# Functions, as it is for loops, cannot be empty. If we want to skip the function body, for example to implement it after, we can use "pass"
def someFunction():
    pass

# Function names follow the same rules as variables
def calculate_sum():
    pass

def _private_function():
    pass

def myFunction2():
    pass
# (These are valid function names)

# Functions can send data back to the code block that executed them by implementing "return" statement
def getData():
    return "your data"

someData = getData()
print(someData)
# (i.e. When the function reaches the "return" statement, it terminates and sends the resulting data back)
# (p.s. If a function doesn't have a "return" statement, it returns "None" by default)

# The primary use of functions is to write some piece of code once, to use it further in a more simple way without rewriting the whole thing many times
def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheitToCelsius(77))
print(fahrenheitToCelsius(95))
print(fahrenheitToCelsius(50))

# We can also document a function by putting a "docstring" inside of it enclosed with three double quote symbols, and it will be returned by {functionName}.__doc__
def fahrenheitToCelsiusDocumented(fahrenheit):
    """
    Docstring for fahrenheitToCelsius
    
    :param fahrenheit: Description
    """
    return (fahrenheit - 32) * 5 / 9

print(fahrenheitToCelsius.__doc__)



