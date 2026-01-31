# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
# Print all key names in the dictionary, one by one.
thisdict = {}
for x in thisdict:
    print(x)
  
# Print all key names in the dictionary, one by one.
for x in thisdict:
    print(x)
    
# You can also use the values() method to return values of a dictionary.
for x in thisdict.values():
    print(x)
    
# You can use the keys() method to return the keys of a dictionary.
for x in thisdict.keys():
    print(x)
    
# Loop through both keys and values, by using the items() method.
for x, y in thisdict.items():
    print(x, y)
