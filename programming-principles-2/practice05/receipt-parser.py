import re
import json

with open("raw.txt", "r", encoding = "UTF-8") as dataStorage:
    rawData = dataStorage.read()
    
    allPrices = re.findall(r"Стоимость\n\d+.?\d+,\d{2}", rawData, re.DOTALL)
    allPrices = list(map(lambda rawString : rawString[10:-3], allPrices))
    allPrices = list(map(lambda stringPrice : int(re.sub(" ", "", stringPrice)), allPrices))
    
    allProductNames = re.findall(r"\d{1,2}[.]\n.*?\n", rawData, re.DOTALL)
    allProductNames = list(map(lambda rawString : re.sub(r"^\d{1,2}.", "", rawString)[1:-1], allProductNames))
    
    totalAmount = 0
    for price in allPrices:
        totalAmount += price
    
    dateAndTime = re.search(r"Время: (.*)", rawData).groups()[0]
    
    paymentMethod = re.search(r"^(.*):", rawData, re.MULTILINE)
    paymentMethod = paymentMethod.group()[:-1]
    
    resultingDict = {}
    resultingDict["Prices"] = allPrices
    resultingDict["ProductNames"] = allProductNames
    resultingDict["TotalAmount"] = totalAmount
    resultingDict["DateAndTime"] = dateAndTime
    resultingDict["PaymentMethod"] = paymentMethod
    
    resultingJson = json.dumps(resultingDict, indent = 4, ensure_ascii = False)
    print(resultingJson)
    
    
    