alice = ["Bananen", "Brot", "Schokolade", "Rotwein"] 
bob = ["Bier", "Bier", "Chips"] 
eve = ["Brot", "Schokolade", "Chips", "Bier", "Wasser"]
finalDict = {}
def addList(input):
    for a in input:
        if not a in finalDict:
            finalDict[a] = 1
        else:
            finalDict[a] = finalDict[a] + 1
        
addList(alice)
addList(bob)
addList(eve)

for x, y in finalDict.items():
  print(str(y) + "x: " + x)