num = int(input())

while num >= 1:
    if num % 2 == 0:
        num /= 2
    elif num == 1: 
        print("YES")
        break
    else:
        print("NO")
        break
    