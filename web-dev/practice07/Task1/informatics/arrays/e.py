n = int(input())

arr = list(map(int, input().split()))
hasSameSign = False

for i in range(1, n):
    if arr[i] * arr[i-1] > 0:
        hasSameSign = True
        break

print("YES" if hasSameSign else "NO")