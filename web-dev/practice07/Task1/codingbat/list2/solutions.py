# count_evens
def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = count_evens(numberArray)
print(f"Number of even integers: {result}")

# big_diff
def big_diff(nums):
    return max(nums) - min(nums)

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = big_diff(numberArray)
print(f"Difference between largest and smallest: {result}")

# centered_average
def centered_average(nums):
    total = sum(nums) - max(nums) - min(nums)
    return total // (len(nums) - 2)

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = centered_average(numberArray)
print(f"Centered average: {result}")

# sum13
def sum13(nums):
    total = 0
    skipNext = False
    for num in nums:
        if num == 13:
            skipNext = True
        elif skipNext:
            skipNext = False
        else:
            total += num
    return total

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = sum13(numberArray)
print(f"Sum (excluding 13 and number after): {result}")

# sum67
def sum67(nums):
    total = 0
    inBlock = False
    for num in nums:
        if num == 6:
            inBlock = True
        elif num == 7 and inBlock:
            inBlock = False
        elif not inBlock:
            total += num
    return total

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = sum67(numberArray)
print(f"Sum (excluding 6 to 7 blocks): {result}")

# has22
def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False

arrayInput = input("Enter numbers separated by spaces: ")
numberArray = list(map(int, arrayInput.split()))
result = has22(numberArray)
print(f"Contains two 2's next to each other? {result}")