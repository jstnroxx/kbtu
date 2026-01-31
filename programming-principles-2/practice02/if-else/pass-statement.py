# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
    pass
# The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.

# During development, you might want to sketch out your program structure before implementing the details. The pass statement allows you to do this without syntax errors.
# Placeholder for future implementation.
age = 16
if age < 18:
    pass # TODO: Add underage logic later
else:
    print("Access granted")
    
# This works correctly with pass.
score = 85
if score > 90:
    pass # This is excellent
print("Score processed")

# Using pass in different branches.
value = 50
if value < 0:
    print("Negative value")
elif value == 0:
    pass # Zero case - no action needed
else:
    print("Positive value")
    
# While we focus on pass with if statements here, it's also commonly used with loops, functions, and classes.
def calculate_discount(price):
  pass # TODO: Implement discount logic
# Function exists but doesn't do anything yet