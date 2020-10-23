import csv
import requests
from datetime import date
from typing import Tuple, List

# a)
def from_web():
    try:
        r = requests.get("https://stadtplan.bonn.de/csv?OD=4379")
    except:
        r.status_code
    with open("data.csv", "w") as f:
        f.write(r.text)


def from_file():
    with open("covid19-data.csv", newline="") as csvdata:
        csvinhalt = csv.reader(csvdata, delimiter=";")
        csvinhalt = list(csvinhalt)
        with open("data.csv", "w", newline="") as csvdatei:
            csvwriter = csv.writer(csvdatei, delimiter=",")
            for datensatz in csvinhalt:
                csvwriter.writerow(datensatz)


def get_data() -> List:
    with open("data.csv", newline="") as csvdatei:
        csvinhalt = csv.DictReader(csvdatei, delimiter=";")
        csvlist = list(csvinhalt)
        for i in csvlist:
            for k in i.keys():
                if i[k] == "":
                    i[k] = "0"
        return csvlist


# b)


def acutly_ill(threshhold: int) -> List:
    data = get_data()
    return list(filter(lambda x: int(x["akut_erkrankt"]) > threshhold, data))


# c)


def sorted_by_date() -> List:
    data = get_data()
    return list(sorted(data, key=lambda row: date.fromisoformat(row["datum"])))


# d)


def positiveSpike() -> Tuple[int, int]:
    data = sorted_by_date()
    highest_count = 0
    highest_date = 0
    for index in range(len(data) - 1):
        increase = int(data[index + 1]["positiv_getest"])
        -int(data[index]["positiv_getest"])
        if increase > highest_count:
            highest_count = increase
            highest_date = data[index + 1]

    return (highest_date, highest_count)


# from_web()
print(sorted_by_date())
print(positiveSpike())
print(acutly_ill(150))