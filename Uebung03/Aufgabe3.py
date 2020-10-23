import json
import requests
from typing import List


def get_pastebin(idList: List[str]):
    textList = []
    for id in idList:
        try:
            response = requests.get(f"https://pastebin.com/raw/{id}")
            response.raise_for_status()
            intermediate = json.loads(response.text)
            textList.append(intermediate)
            for index in range(len(textList)):
                for key in range(10):
                    try:
                        print(textList[index][str(key)])
                    except KeyError as err:
                        print(err)

        except requests.exceptions.HTTPError as err:
            print(f"The request for code: {id} gave the error:")
            print(err)
        except json.JSONDecodeError as jsonErr:
            print("JSONDecodeError:")
            print(jsonErr)


get_pastebin(["LIaSudG3", "pmZ2Q0gU", "AeUNgdAb"])