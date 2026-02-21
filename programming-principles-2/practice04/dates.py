import datetime as dt

# 1
currentDate = dt.datetime.now()
currentMinusFive = currentDate - dt.timedelta(days=5)
print(currentMinusFive, "\n")

# 2
yesterday = currentDate - dt.timedelta(days=1)
tomorrow = currentDate + dt.timedelta(days=1)
print(yesterday.strftime("%Y-%m-%d"))
print(currentDate.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"), "\n")

# 3
noMicroseconds = currentDate.replace(microsecond=0)
print(noMicroseconds, "\n")

# 4
exampleDate = dt.date(2026, 2, 1)
fixedCurrent = currentDate.date()
dateDifference = fixedCurrent - exampleDate
print(dateDifference.total_seconds())

