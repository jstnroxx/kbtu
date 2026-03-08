# sleep_in
def sleep_in(weekday, vacation):
    return not weekday or vacation

isWeekday = input("Is it a weekday? (yes/no): ").lower() == "yes"
isVacation = input("Are you on vacation? (yes/no): ").lower() == "yes"
result = sleep_in(isWeekday, isVacation)
print(f"Can you sleep in? {result}")

# monkey_trouble
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

aSmile = input("Is monkey A smiling? (yes/no): ").lower() == "yes"
bSmile = input("Is monkey B smiling? (yes/no): ").lower() == "yes"
result = monkey_trouble(aSmile, bSmile)
print(f"Are we in trouble? {result}")

# sum_double
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b

numA = int(input("Enter first number: "))
numB = int(input("Enter second number: "))
result = sum_double(numA, numB)
print(f"Result: {result}")

# diff21
def diff21(n):
    if n > 21:
        return 2 * (n - 21)
    else:
        return 21 - n

number = int(input("Enter a number: "))
result = diff21(number)
print(f"Difference from 21: {result}")

# parrot_trouble
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

isTalking = input("Is the parrot talking? (yes/no): ").lower() == "yes"
currentHour = int(input("Enter the hour (0-23): "))
result = parrot_trouble(isTalking, currentHour)
print(f"Are we in trouble? {result}")

# makes10
def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

numA = int(input("Enter first number: "))
numB = int(input("Enter second number: "))
result = makes10(numA, numB)
print(f"Makes 10? {result}")

# near_hundred
def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

number = int(input("Enter a number: "))
result = near_hundred(number)
print(f"Near 100 or 200? {result}")

# pos_neg
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)

numA = int(input("Enter first number: "))
numB = int(input("Enter second number: "))
checkNegative = input("Check if both negative? (yes/no): ").lower() == "yes"
result = pos_neg(numA, numB, checkNegative)
print(f"Result: {result}")

# not_string
def not_string(str):
    if str.startswith("not"):
        return str
    else:
        return "not " + str

inputString = input("Enter a string: ")
result = not_string(inputString)
print(f"Result: {result}")

# missing_char
def missing_char(str, n):
    return str[:n] + str[n+1:]

inputString = input("Enter a string: ")
indexToRemove = int(input("Enter index to remove: "))
result = missing_char(inputString, indexToRemove)
print(f"Result: {result}")

# front_back
def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]

inputString = input("Enter a string: ")
result = front_back(inputString)
print(f"Result: {result}")

# front3
def front3(str):
    if len(str) < 3:
        front = str
    else:
        front = str[:3]
    return front * 3

inputString = input("Enter a string: ")
result = front3(inputString)
print(f"Result: {result}")