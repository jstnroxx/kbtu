# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

# Add 10 to argument "a", and return the result
x = lambda a : a + 10
print(x(5))

# Multiply argument "a" with argument "b" and return the result
x = lambda a, b : a * b
print(x(5, 6))

# Summarize argument "a", "b", and "c" and return the result
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Lambda usage as an anonymous function inside another function
def myMultiplier(n):
    return lambda a : a * n

mydoubler = myMultiplier(2)
mytripler = myMultiplier(3)

print(mydoubler(11))
print(mytripler(11))
# (We use lambda functions when an anonymous function is required for a short period of time)

# Anonymous function vs regular one
def mySquare(x):
    return x * x
# (Regular version)

myLambdaSquare = lambda x : x * x
# (Lambda version)

print(mySquare(5), myLambdaSquare(5))
