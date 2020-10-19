import time
import configparser

switcher = {
    1: "eins",
    2: "zwei",
    3: "drei",
    4: "vier",
    5: "fünf",
    6: "sechs",
    7: "sieben",
    8: "acht",
    9: "neun",
    10: "zehn",
    11: "elf",
    12: "zwölf",
}


def switch(input):
    if input > 12:
        return switcher[input - 12]
    return switcher[input]


def print_time():
    now = time.localtime()
    hour = now.tm_hour
    minute = now.tm_min
    if 5 < minute <= 15:
        print(f"Es ist {switch(10)} nach {switch(hour)}.")
    elif 15 < minute <= 25:
        print(f"Es ist {switch(20)} nach {switch(hour)}.")
    elif 25 < minute <= 35:
        print(f"Es ist halb {switch(hour+1)}.")
    elif 35 < minute < 45:
        print(f"Es ist zwanzig vor {switch(hour+1)}.")
    elif 45 < minute <= 55:
        print(f"Es ist {switch(10)} vor {switch(hour+1)}.")
    elif 55 < minute <= 59:
        print(f"Es ist {switch(hour+1)}.")
    elif 0 < minute < 5:
        print(f"Es ist {switch(hour)}.")


config = configparser.ConfigParser()
conf = config.read("/home/knniff/python-projects/python-vorkurs/Uebung05/conf.ini")
time_intervall = int(config["Time"]["time"])
while True:
    print_time()
    time.sleep(time_intervall)