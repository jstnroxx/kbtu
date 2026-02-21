import json as JSON

# 1
jsonData = ""

with open("sample-data.json") as dataFile:
    jsonData = JSON.loads(dataFile.read())
    
print("Interface Status")
print("========================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  -------  ------")

if (jsonData == ""):
    print("Failed to retrieve data.")
else:
    for object in jsonData["imdata"]:
        attributes = object["l1PhysIf"]["attributes"]
        
        dn = attributes["dn"]
        descr = attributes["descr"]
        speed = attributes["speed"]
        mtu = attributes["mtu"]
        
        print(f"{dn:<50} {descr:<21} {speed:<8} {mtu:<6}")