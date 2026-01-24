# We can use quotes inside a string, as long as they don't match the quotes surrounding the string.
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# We can assign a multiline string to a variable by using three quotes.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# P.S. Or three singular ones.
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) # In the result, the line breaks are inserted at the same position as in the code.

# Getting the character at specific index.
a = "Hello, World!"
print(a[1])

# Looping through a string.
for x in "banana":
  print(x)
  
# To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

# Prints only if "free" is present.
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
# Check if "expensive" is NOT present in the following text.
txt = "The best things in life are free!"
print("expensive" not in txt)

# Get the characters from position 2 to position 5 (not inclusive). (Slicing)
b = "Hello, World!"
print(b[2:5])

# Get the characters from the start to position 5 (not included).
b = "Hello, World!"
print(b[:5])

# Get the characters from position 2, and all the way to the end.
b = "Hello, World!"
print(b[2:])

""" 
Get the characters with negative indexing.
From: "o" in "World!" (position -5)
To, but not inclusively: "d" in "World!" (position -2):
"""
b = "Hello, World!"
print(b[-5:-2])

# The upper() and lower() METHODS return the string in upper and lower case respectively.
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

# The strip() method removes any whitespace from the beginning or the end.
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# The replace() method replaces a string with another string.
a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator.
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals.
# E.g. Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# A placeholder can contain Python code, like math operations.
# E.g. Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)

# Python built-in string methods.
"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""
# P.S. All string methods return new values. They do not change the original string.