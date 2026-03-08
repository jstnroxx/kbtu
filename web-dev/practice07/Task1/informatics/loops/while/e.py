n = int(input())

counter = 0
power = 1

while counter <= n:
    if power >= n:
        print(counter)
        break
    power *= 2
    counter += 1