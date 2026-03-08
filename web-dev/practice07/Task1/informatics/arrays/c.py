n = int(input())

arr = list(map(int, input().split()))

positiveCount = sum(1 for x in arr if x > 0)

print(positiveCount)