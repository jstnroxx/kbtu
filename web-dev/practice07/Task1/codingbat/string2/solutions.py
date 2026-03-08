# double_char
def double_char(str):
    result = ""
    for char in str:
        result += char * 2
    return result

inputString = input("Enter a string: ")
result = double_char(inputString)
print(f"Result: {result}")

# count_hi
def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i:i+2] == "hi":
            count += 1
    return count

inputString = input("Enter a string: ")
result = count_hi(inputString)
print(f"Number of 'hi': {result}")

# cat_dog
def cat_dog(str):
    catCount = 0
    dogCount = 0
    for i in range(len(str) - 2):
        if str[i:i+3] == "cat":
            catCount += 1
        elif str[i:i+3] == "dog":
            dogCount += 1
    return catCount == dogCount

inputString = input("Enter a string: ")
result = cat_dog(inputString)
print(f"Same number of 'cat' and 'dog'? {result}")

# count_code
def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if str[i:i+2] == "co" and str[i+3] == "e":
            count += 1
    return count

inputString = input("Enter a string: ")
result = count_code(inputString)
print(f"Number of 'co_e' patterns: {result}")

# end_other
def end_other(a, b):
    aLower = a.lower()
    bLower = b.lower()
    return aLower.endswith(bLower) or bLower.endswith(aLower)

stringA = input("Enter first string: ")
stringB = input("Enter second string: ")
result = end_other(stringA, stringB)
print(f"One ends with the other? {result}")

# xyz_there
def xyz_there(str):
    for i in range(len(str) - 2):
        if str[i:i+3] == "xyz":
            if i == 0 or str[i-1] != ".":
                return True
    return False

inputString = input("Enter a string: ")
result = xyz_there(inputString)
print(f"Contains 'xyz' (not preceded by '.')? {result}")