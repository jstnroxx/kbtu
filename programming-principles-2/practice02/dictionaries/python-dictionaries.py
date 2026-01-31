# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Print the "brand" value of the dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Duplicate values will overwrite existing values.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Print the number of items in the dictionary.
print(len(thisdict))

# String, int, boolean, and list data types.
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Using the dict() method to make a dictionary.
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Dictionary is a collection which is ordered** and changeable. No duplicate members.