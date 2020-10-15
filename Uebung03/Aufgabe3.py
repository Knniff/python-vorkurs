import json
import requests


def get_pastebin(idList):
    textList = []
    for id in idList:
        try:
            response = requests.get(f"https://pastebin.com/raw/{id}")
        except response.raise_for_status as err:
            print("RequestError:")
            print(err)
        try:
            intermediate = json.loads(response.text)
            textList.append(intermediate)
        except json.JSONDecodeError as jsonErr:
            print("JSONDecodeError:")
            print(jsonErr)
        for index in range(len(textList)):
            for key in textList[index]:
                print(textList[index][key])


get_pastebin(["LIaSudG3", "pmZ2Q0gU", "AeUNgdAb"])