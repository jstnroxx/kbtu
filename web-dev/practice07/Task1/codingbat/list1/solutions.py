# first_last6
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = first_last6(numberArray)
print(f"Has 6 at first or last position? {result}")

# same_first_last
def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = same_first_last(numberArray)
print(f"First and last are same? {result}")

# make_pi
def make_pi():
    return [3, 1, 4]

result = make_pi()
print(f"First 3 digits of pi: {result}")

# common_end
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

arrayA = input("Enter first array (space-separated): ")
listA = list(map(int, arrayA.split()))
arrayB = input("Enter second array (space-separated): ")
listB = list(map(int, arrayB.split()))
result = common_end(listA, listB)
print(f"Common first or last element? {result}")

# sum3
def sum3(nums):
    return sum(nums)

arrayInput = input("Enter 3 numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = sum3(numberArray)
print(f"Sum: {result}")

# rotate_left3
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

arrayInput = input("Enter 3 numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = rotate_left3(numberArray)
print(f"Rotated left: {result}")

# reverse3
def reverse3(nums):
    return nums[::-1]

arrayInput = input("Enter 3 numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = reverse3(numberArray)
print(f"Reversed: {result}")

# max_end3
def max_end3(nums):
    maxValue = max(nums[0], nums[-1])
    return [maxValue, maxValue, maxValue]

arrayInput = input("Enter 3 numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = max_end3(numberArray)
print(f"All set to max of first/last: {result}")

# sum2
def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + nums[1]

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = sum2(numberArray)
print(f"Sum of first 2 elements: {result}")

# middle_way
def middle_way(a, b):
    return [a[1], b[1]]

arrayA = input("Enter first array of 3 numbers (space-separated): ")
listA = list(map(int, arrayA.split()))
arrayB = input("Enter second array of 3 numbers (space-separated): ")
listB = list(map(int, arrayB.split()))
result = middle_way(listA, listB)
print(f"Middle elements: {result}")

# make_ends
def make_ends(nums):
    return [nums[0], nums[-1]]

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = make_ends(numberArray)
print(f"First and last elements: {result}")

# has23
def has23(nums):
    return 2 in nums or 3 in nums

arrayInput = input("Enter 2 numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = has23(numberArray)
print(f"Contains 2 or 3? {result}")