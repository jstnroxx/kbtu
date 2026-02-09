# The "filter()" function creates a list of items for which a function returns True

# Filter out even numbers from a list
myNumbers = [1, 2, 3, 4, 5, 6, 7, 8]
oddNumbers = list(filter(lambda x : x % 2 != 0, myNumbers))
print(oddNumbers)

# Filtering out negative numbers
myNumbers = [0, -1, 2, -3, 4, -5, -6]
positiveNumbers = list(filter(lambda x : x >= 0, myNumbers))
print(positiveNumbers)

# Getting rid of names that start with the letter "B"
myNames = ["Alex", "Maxim", "Josh", "Basil", "Yan", "Boris"]
filteredNames = list(filter(lambda name : name[0] != "B", myNames))
print(filteredNames)

# Filtering dictionaries by value more than 100
myValues = {
    "Value1" : 1,
    "ValueNegative" : -1,
    "ValueZero" : 0,
    "Value2" : 2,
    "BigValue" : 133722842069,
    "NotThatBigOfAValue" : 100.05
}
filteredValues = dict(filter(lambda item : item[1] > 100, myValues.items()))
print(filteredValues)