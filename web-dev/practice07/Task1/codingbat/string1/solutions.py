# hello_name
def hello_name(name):
    return "Hello " + name + "!"

userName = input("Enter a name: ")
result = hello_name(userName)
print(f"Result: {result}")

# make_abba
def make_abba(a, b):
    return a + b + b + a

stringA = input("Enter first string: ")
stringB = input("Enter second string: ")
result = make_abba(stringA, stringB)
print(f"Result: {result}")

# make_tags
def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

tagName = input("Enter tag name: ")
wordContent = input("Enter word: ")
result = make_tags(tagName, wordContent)
print(f"Result: {result}")

# make_out_word
def make_out_word(out, word):
    return out[:2] + word + out[2:]

outerString = input("Enter outer string (length 4): ")
innerWord = input("Enter inner word: ")
result = make_out_word(outerString, innerWord)
print(f"Result: {result}")

# extra_end
def extra_end(str):
    return str[-2:] * 3

inputString = input("Enter a string: ")
result = extra_end(inputString)
print(f"Result: {result}")

# first_two
def first_two(str):
    if len(str) <= 2:
        return str
    return str[:2]

inputString = input("Enter a string: ")
result = first_two(inputString)
print(f"Result: {result}")

# first_half
def first_half(str):
    return str[:len(str)//2]

inputString = input("Enter a string (even length): ")
result = first_half(inputString)
print(f"Result: {result}")

# without_end
def without_end(str):
    return str[1:-1]

inputString = input("Enter a string: ")
result = without_end(inputString)
print(f"Result: {result}")

# combo_string
def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a

stringA = input("Enter first string: ")
stringB = input("Enter second string: ")
result = combo_string(stringA, stringB)
print(f"Result: {result}")

# non_start
def non_start(a, b):
    return a[1:] + b[1:]

stringA = input("Enter first string: ")
stringB = input("Enter second string: ")
result = non_start(stringA, stringB)
print(f"Result: {result}")

# left2
def left2(str):
    return str[2:] + str[:2]

inputString = input("Enter a string: ")
result = left2(inputString)
print(f"Result: {result}")