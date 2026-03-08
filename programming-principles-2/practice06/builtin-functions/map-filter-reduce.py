from functools import reduce

aList = [-3, -2, -1, 0, 1, 2, 3]

# 1. Use map() and filter() on lists.
squaredNumbers = list(map(lambda element : element * element, aList))   # Squares each number in a list.
print(squaredNumbers)

rangeInput = abs(int(input('Please enter a range (e.g. "1"): ')))
filteredNumbers = list(filter(lambda element : abs(element) <= (0 + rangeInput), aList))    # Filters a list to show numbers by arbitrary proximity to zero.
print(filteredNumbers)

# 2. Aggregate with reduce() (from functools).
negativeNumbers = list(filter(lambda element : element < 0, aList))
negativeSum = reduce(lambda accumulator, current : accumulator + current, negativeNumbers)
print(negativeSum)

# 4. Demonstrate type checking and conversions.
# 4.1. Type checking.
print(type(1))
print(type("abc."))
print(type(["a", "b", "c"]))

# 4.2. Type conversion.
print(float(1))
print(str(123) + " is a string.")
print(tuple(["a", "b", "c"]))