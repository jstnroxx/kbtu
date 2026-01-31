# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Make a copy of a list with the list() method.
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Make a copy of a list with the : operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)