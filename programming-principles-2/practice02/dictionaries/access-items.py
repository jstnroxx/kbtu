# You can access the items of a dictionary by referring to its key name, inside square brackets.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result.
x = thisdict.get("model")

# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

# Get a list of the key:value pairs (tuples).
x = thisdict.items()

# Check if "model" is present in the dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")