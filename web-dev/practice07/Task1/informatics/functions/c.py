def xor(x, y):
    if x or y:
        if x != y:
            return 1
    return 0

x, y = input().split()
print(xor(int(x), int(y)))