# Python supports the usual logical conditions from mathematics.
"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

# An "if statement" is written by using the if keyword.
a = 33
b = 200
if b > a:
    print("b is greater than a")
    
# Checking if a number is positive.
number = 15
if number > 0:
    print("The number is positive")
    
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
# If statement, without indentation (will raise an error).
"""
a = 33
b = 200
if b > a:
print("b is greater than a") -> you will get an error
"""

# Multiple statements in an if block.
age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")
    
# Boolean variables can be used directly in if statements without comparison operators.
is_logged_in = True
if is_logged_in:
    print("Welcome back!")
    


