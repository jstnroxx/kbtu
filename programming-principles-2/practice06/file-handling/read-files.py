# 2. Read and print file contents.
try:
    with open("sample.txt") as testFile:    # "r" by default!
        print(testFile.read())
except:
    print("No file found to read.")