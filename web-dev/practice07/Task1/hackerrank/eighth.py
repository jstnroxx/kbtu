numCommands = int(input())
workingList = []

for _ in range(numCommands):
    commandParts = input().split()
    commandName = commandParts[0]
    
    if commandName == "insert":
        workingList.insert(int(commandParts[1]), int(commandParts[2]))
    elif commandName == "print":
        print(workingList)
    elif commandName == "remove":
        workingList.remove(int(commandParts[1]))
    elif commandName == "append":
        workingList.append(int(commandParts[1]))
    elif commandName == "sort":
        workingList.sort()
    elif commandName == "pop":
        workingList.pop()
    elif commandName == "reverse":
        workingList.reverse()