def isLeap(year):
    isLeapYear = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                isLeapYear = True
            else:
                isLeapYear = False
        else:
            isLeapYear = True
            
    return isLeapYear

year = int(input())
print(isLeap(year))