n = int(input())

arr = list(map(int, input().split()))

evenElements = [x for x in arr if x % 2 == 0]

print(*evenElements)