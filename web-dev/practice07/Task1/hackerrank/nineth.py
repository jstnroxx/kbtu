inputString = input()
swappedString = ""

for char in inputString:
    if char.isupper():
        swappedString += char.lower()
    elif char.islower():
        swappedString += char.upper()
    else:
        swappedString += char

print(swappedString)