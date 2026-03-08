xLimit = int(input())
yLimit = int(input())
zLimit = int(input())
nTarget = int(input())

coordinatesList = [[i, j, k] for i in range(xLimit + 1) for j in range(yLimit + 1) for k in range(zLimit + 1) if (i + j + k) != nTarget]

print(coordinatesList)