a = int(input())
b = int(input())
c = int(input())
d = int(input())

for number in range(a, b):
    if number % d == c:
        print(number, end=" ")