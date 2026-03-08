n = int(input())

arr = list(map(int, input().split()))

greaterThanPreviousCount = sum(1 for i in range(1, n) if arr[i] > arr[i-1])

print(greaterThanPreviousCount)