x = int(input())

divisors = 0

for number in range(1, x + 1):
    if x % number == 0:
        divisors += 1

print(divisors)