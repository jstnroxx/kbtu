x = int(input())

for number in range(2, x + 1):
    if x % number == 0:
        if number and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)):
            print(number)
            break
