import json
import requests


class StadtWetter:
    town = ""
    def __init__(self):
        self.town = input("Geben sie ihre Stadt an:")
        #self.getwebdata()
    def getwebdata(self):
        try:
            r = requests.get(f"https://wttr.in/{self.town}?format=j1")
        except:
            r.status_code

        with open(f"{self.town}.json", "w") as f:
            f.write(r.text)

    def getDesc(self):
        with open(f"{self.town}.json", "r") as jsondatei:
            data = json.load(jsondatei) 
        print(data["current_condition"][0]["weatherDesc"][0])

    def getMaxTemp(self):
        with open(f"{self.town}.json", "r") as jsondatei:
            data = json.load(jsondatei) 
        print(data["weather"][1]["maxtempC"])
test = StadtWetter()
test.getDesc()
test.getMaxTemp()