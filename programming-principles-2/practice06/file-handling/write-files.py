# 1. Create a text file and write sample data.
with open("sample.txt", "w") as testFile:
    testFile.write("Some sample data.")
    
# 3. Append new lines and verify content.
with open("sample.txt", "a") as testFile:
    testFile.write("\nSome new information!")
    
with open("sample.txt") as testFile:    # "r" by default!
    print(testFile.read())