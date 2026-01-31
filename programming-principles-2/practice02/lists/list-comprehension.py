# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# With list comprehension you can do all that with only one line of code.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# The Syntax.
# newlist = [expression for item in iterable if condition == True]

# Only accept items that are not "apple".
newlist = [x for x in fruits if x != "apple"]

# With no if statement.
newlist = [x for x in fruits]

# You can use the range() function to create an iterable.
newlist = [x for x in range(10)]

# Accept only numbers lower than 5.
newlist = [x for x in range(10) if x < 5]

# Set the values in the new list to upper case.
newlist = [x.upper() for x in fruits]

# Set all values in the new list to 'hello'.
newlist = ['hello' for x in fruits]

# Return "orange" instead of "banana".
newlist = [x if x != "banana" else "orange" for x in fruits]

