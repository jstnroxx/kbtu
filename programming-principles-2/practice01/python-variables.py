# Variables do not need a datatype to be written when declaring, we assign the value directly.
x = 5
y = "John"
print(x)
print(y)

# Datatypes are dynamically assigned.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Typecasting looks like this.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# With the type() function we can get the current datatype of a variable.
x = 5
y = "John"
print(type(x))
print(type(y))

# Variable names ARE case-sensitive.
a = 4
A = "Sally" #A will not overwrite a

# Examples of legal variable naming.
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Assigning multiple values in a singular line.
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Setting one value for multiple variables.
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpacking values from a collection into a set of variables.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# String concatenation while printing.
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# "x" in the case below is a global variable.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# We can create a variable with the same name but inside another scope, they will be separate.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Also, we can create and access global variables from local scopes by using the keyword "global".
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)