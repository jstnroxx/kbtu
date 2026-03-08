# string_times
def string_times(str, n):
    return str * n

inputString = input("Enter a string: ")
repeatCount = int(input("Enter number of times to repeat: "))
result = string_times(inputString, repeatCount)
print(f"Result: {result}")

# front_times
def front_times(str, n):
    if len(str) < 3:
        front = str
    else:
        front = str[:3]
    return front * n

inputString = input("Enter a string: ")
repeatCount = int(input("Enter number of times to repeat front: "))
result = front_times(inputString, repeatCount)
print(f"Result: {result}")

# string_bits
def string_bits(str):
    return str[::2]

inputString = input("Enter a string: ")
result = string_bits(inputString)
print(f"Result: {result}")

# string_splosion
def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
    return result

inputString = input("Enter a string: ")
result = string_splosion(inputString)
print(f"Result: {result}")

# last2
def last2(str):
    if len(str) < 2:
        return 0
    count = 0
    lastTwo = str[-2:]
    for i in range(len(str) - 2):
        if str[i:i+2] == lastTwo:
            count += 1
    return count

inputString = input("Enter a string: ")
result = last2(inputString)
print(f"Count: {result}")

# array_count9
def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = array_count9(numberArray)
print(f"Number of 9's: {result}")

# array_front9
def array_front9(nums):
    checkLength = min(4, len(nums))
    for i in range(checkLength):
        if nums[i] == 9:
            return True
    return False

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = array_front9(numberArray)
print(f"Has 9 in first 4 elements? {result}")

# array123
def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = array123(numberArray)
print(f"Contains sequence 1, 2, 3? {result}")

# string_match
def string_match(a, b):
    shorterLength = min(len(a), len(b))
    count = 0
    for i in range(shorterLength - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count

stringA = input("Enter first string: ")
stringB = input("Enter second string: ")
result = string_match(stringA, stringB)
print(f"Number of matching substrings: {result}")