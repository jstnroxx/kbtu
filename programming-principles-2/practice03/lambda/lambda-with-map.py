# The "map()" function applies a function to every item in an iterable

# Double all numbers in a list
myNumbers = [1, 2, 3, 4, 5]
doubledNumbers = list(map(lambda x : x * 2, myNumbers))
print(doubledNumbers)

# Updating names in a list
myNames = ["Danil", "Mansur", "Maxim"]
myNames = list(map(lambda name : name + "IsBro", myNames))
print(myNames)

# Doubling all positive numbers in a sequence
myNumbers = [-3, -2, -1, 0, 1, 2, 3]
doubledPositiveStuff = list(map(lambda number : number * 2 if number > 0 else number, myNumbers))
print(doubledPositiveStuff)