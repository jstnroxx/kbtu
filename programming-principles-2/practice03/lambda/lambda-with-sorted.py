# The "sorted()" function can use a lambda as a key for custom sorting

# Sort a list of tuples by the second element
myStudents = [("Maxim", 19), ("Danil", 20), ("Andrew", 39), ("Mansur", 18)]
sortedStudents = sorted(myStudents, key=lambda x : x[1])
print(sortedStudents)

# Sorting some "theoretical number occurences" we found somewhere in ascending order
myOccurences = {
    "a" : 0, 
    "b" : 2,
    "c" : 6,
    "d" : 0,
    "e" : 1,
    "f" : 5
}
sortedOccurences = sorted(myOccurences, key=lambda x : myOccurences[x])
print(sortedOccurences)

# Sorting the list of strings by their length ascending
myFood = ["Apple", "Pineapple", "Burger", "dwichSan", "Cucumber", "Pea"]
sortedFood = sorted(myFood, key=lambda food : len(food))
print(sortedFood)

# Sorting numbers by their absolute value in descending order updating the original list
myNumbers = [1, 9, -2, 0, 2, 2, 3, 54, -23, 68, 88, 1.5]
myNumbers = sorted(myNumbers, key=lambda x : x if (x >= 0) else (x * -1), reverse=True)
print(myNumbers)
