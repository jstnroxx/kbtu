inputNumber = int(input())
paddingWidth = len(bin(inputNumber)[2:])

for i in range(1, inputNumber + 1):
    decimalStr = str(i).rjust(paddingWidth)
    octalStr = oct(i)[2:].rjust(paddingWidth)
    hexStr = hex(i)[2:].upper().rjust(paddingWidth)
    binaryStr = bin(i)[2:].rjust(paddingWidth)
    print(decimalStr, octalStr, hexStr, binaryStr)