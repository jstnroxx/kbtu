# Iterator and generator examples
# An iterator is an object that contains a countable number of values
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values

# All iterable objects (lists, tuples, dictionaries, sets and even strings) have iter(), which is used to get an iterator, and next(), which goes to the next iteration, methods
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# To implement iter() and next() in our custom data structures, we need to define __iter__ and __next__ methods inside the class
class MyNumbers:
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        if self.x <= 20:
            result = self.x
            self.x += 1
            return result    
        else:
            raise StopIteration # To limit iteration bounds we throw a StopIteration exception
        
numbersObject = MyNumbers()
numbersIterator = iter(numbersObject)

# Looping through an iterator to get all the values from it
for num in numbersIterator:
    print(num)
    
# Generators are functions that can pause and resume their execution
# When a generator function is called, it returns a generator object, which is an iterator

# Basic three number yielding generator
def my_generator():
    yield 1 # The yield keyword is what makes a function a generator
    yield 2 # When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off
    yield 3
    
for value in my_generator():
    print(value)
    
# Number yielding generator 
def count_up_to(n):
    count = 1
    while count <= n:
        yield count # Unlike return, which terminates the function, yield pauses it and can be called multiple times
        count += 1
        
for num in count_up_to(5):
    print(num)
    
# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# You can manually iterate through a generator using the next() function
def simple_gen():
    yield "Emil"
    yield "Tobias"
    yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

# The send() method allows you to send a value to the generator
def echo_generator():
    while True:
        received = yield
        print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

# The close() method stops the generator
def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()

# EXERCISES
# 1
def squareGen(n):
    for num in range(n):
        yield num * num
        
print("\n")
for square in squareGen(5):
    print(square)
    
# 2
def evenGen(n):
    for num in range(n + 1):
        if (num % 2 == 0):
            yield num
            
n = 16
print("\n")
for even in evenGen(n):
    if (even == n or even == n - 1):
        print(even)
    else:
        print(even, end=", ")
        
# 3
def divGen(n):
    for num in range(n + 1):
        if (num % 3 == 0 and num % 4 == 0):
            yield num

print("\n")
for divisible in divGen(100):
    print(divisible)
    
# 4
def squares(a, b):
    for num in range(a, b + 1):
        yield num * num
        
print("\n")
for square in squares(5, 10):
    print(square)

# 5
def toZero(n):
    for num in range(n, -1, -1):
        yield num
        
print("\n")
for number in toZero(10):
    print(number)