# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove the first occurrence of "banana".
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Remove the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index.
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Delete the entire list.
thislist = ["apple", "banana", "cherry"]
del thislist

# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)