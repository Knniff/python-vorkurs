import json
import requests


class StadtWetterv1:
    town = ""
    Wetterdaten = ""

    def __init__(self):
        self.town = input("Geben sie ihre Stadt an:")
        self.get_web_data()

    def get_web_data(self):
        try:
            response = requests.get(f"https://wttr.in/{self.town}?format=j1")
        except:
            response.status_code
        with open(f"{self.town}.json", "w") as f:
            f.write(response.text)

    def get_desc(self):
        with open(f"{self.town}.json", "r") as jsondatei:
            data = json.load(jsondatei)
        print(data["current_condition"][0]["weatherDesc"][0])

    def get_max_temp(self):
        with open(f"{self.town}.json", "r") as jsondatei:
            data = json.load(jsondatei)
        print(data["weather"][1]["maxtempC"])


v1 = StadtWetterv1()
v1.get_desc()
v1.get_max_temp()


class StadtWetterv2:
    Wetterdaten = ""

    def __init__(self):
        self.get_web_data(input("Geben sie ihre Stadt an:"))

    def get_web_data(self, town):
        try:
            response = requests.get(f"https://wttr.in/{town}?format=j1")
        except:
            response.status_code
        self.Wetterdaten = json.loads(response.text)

    def get_desc(self):
        print(self.Wetterdaten["current_condition"][0]["weatherDesc"][0])

    def get_max_temp(self):
        print(
            "Die Höchst Temperatur morgen beträgt: "
            + self.Wetterdaten["weather"][1]["maxtempC"]
            + "°C"
        )


v2 = StadtWetterv2()
v2.get_desc()
v2.get_max_temp()