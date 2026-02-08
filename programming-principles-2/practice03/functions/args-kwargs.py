# "*args" and "**kwargs" allow functions to accept an unknown amount of arguments
# The "*args" parameter allows a function to accept any number of positional arguments, inside the function, args becomes a TUPLE containing all the passed arguments
def argsTest(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

argsTest("Emil", "Tobias", "Linus")

# We can combine regular parameters with "*args", regular parameters must come before "*args"
def greetGuys(greeting, *names):
    for name in names:
        print(greeting, name)

greetGuys("Hello", "Maxim", "Danil", "Mansur")

# A function that calculates the sum of any number of values
def mySum(*numbers):
    tempSum = 0
    
    for number in numbers:
        tempSum += number
        
    return tempSum

print(mySum(1))
print(mySum(123, -5, 2))
print(mySum(1, 2, 3, 4, 5, 6, 7))
print(mySum())

# A function to find the maximum value from provided values
def maxVal(*numbers):
    if len(numbers) == 0:
        return None

    maxNum = numbers[0]

    for num in numbers:
        if num > maxNum:
            maxNum = num
        
    return maxNum

print(maxVal(3, 7, 2, 5, 1))

# The "**kwargs" parameter allows a function to accept any number of keyword arguments, inside the function, "kwargs" becomes a dictionary containing all the keyword arguments
def kwargsTest(**myStuff):
    print("Type:", type(myStuff))
    print("Name:", myStuff["name"])
    print("Age:", myStuff["age"])
    print("All data:", myStuff)

kwargsTest(name = "Maxim", age = 19, city = "Almaty")

# We can use both "*args" and "**kwargs" in the same function. The order must be: 1) regular parameters, 2) *args, 3) **kwargs.
def argsKwargsExample(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

argsKwargsExample("User Info", "Maxim1", "Maxim2", age = 19, city = "Almaty")

# If we have values stored in a list, we can use "*" to unpack them into individual arguments
def mySum2(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = mySum2(*numbers) # Same as: mySum(1, 2, 3)
print(result)

# If we have keyword arguments stored in a dictionary, we can use "**" to unpack them
def greetMe(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Maxim", "lname": "Smirnov"}
greetMe(**person) # Same as: greetMe(fname="Maxim", lname="Smirnov")

