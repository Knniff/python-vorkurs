alice = ["Bananen", "Brot", "Schokolade", "Rotwein"]
bob = ["Bier", "Bier", "Chips"]
eve = ["Brot", "Schokolade", "Chips", "Bier", "Wasser"]


def add_list(input: list):
    finalDict = {}
    for a in input:
        if not a in finalDict:
            finalDict[a] = 1
        else:
            finalDict[a] += 1
    for x, y in finalDict.items():
        print(str(y) + "x: " + x)


add_list(alice + bob + eve)
