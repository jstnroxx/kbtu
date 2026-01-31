# The bool() function allows you to evaluate any value, and give you True or False in return.
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Almost any value is evaluated to True if it has some sort of content. The following will return True.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# The following will return False.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False.
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))