n = int(input())

sum = 0

for _ in range(n):
    number = int(input())
    if number == 0:
        sum += 1
    
print(sum)