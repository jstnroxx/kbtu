n = int(input())

number = 2

while number <= n:
    if n % number == 0:
        if number and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)):
            print(number)
            break
    number += 1


    
