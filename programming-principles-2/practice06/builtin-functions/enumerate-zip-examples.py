aList = [-3, -2, -1, 0, 1, 2, 3]

# 3. Use enumerate() and zip() for paired iteration.
indexedNumbers = list(enumerate(aList))
alteredNumbers = list(map(lambda pair : sum(pair), indexedNumbers))
print(alteredNumbers)

reversedNumbers = sorted(aList, reverse = True)
pairedNumbers = list(zip(aList, reversedNumbers))
canceledNumbers = list(map(lambda pair : sum(pair), pairedNumbers))
print(canceledNumbers)