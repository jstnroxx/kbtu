a = int(input())
b = int(input())

for number in range(a, b + 1):
    if number % 2 == 0:
        print(number, end=" ")