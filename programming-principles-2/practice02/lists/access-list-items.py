# List items are indexed and you can access them by referring to the index number.
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# This example returns the items from the beginning to, but NOT including, "kiwi".
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# This example returns the items from "cherry" to the end.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1).
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if "apple" is present in the list.
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
    
