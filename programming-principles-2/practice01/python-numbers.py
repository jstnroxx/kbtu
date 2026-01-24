# There are three number datatypes.
"""
int
float
complex
"""

# Floats can have scientific values with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex numbers are written with a "j" as the imaginary part.
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# P.S. You cannot convert complex numbers into another number type.

# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers.
import random

print(random.randrange(1, 10))