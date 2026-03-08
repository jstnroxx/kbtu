a = int(input())
b = int(input())

for number in range(a, b):
    if (number ** 0.5) % 1 == 0:
        print(number, end=" ")