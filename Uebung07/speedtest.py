import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

finn_zeiten = []
jonas_zeiten = []
participant_list = [
    ("2020-10-12", 210),
    ("2020-10-13", 180),
    ("2020-10-14", 180),
    ("2020-10-15", 165),
    ("2020-10-16", 160),
    ("2020-10-19", 165),
    ("2020-10-20", 155),
    ("2020-10-21", None),
    ("2020-10-22", None),
    ("2020-10-23", None),
]


def finn():
    participant_dataframe = pd.DataFrame(participant_list, columns=["date", "number"])
    participant_dataframe = participant_dataframe.set_index(
        "date", drop=True, append=False
    )
    return participant_dataframe


def jonas():
    data = pd.DataFrame(
        {
            "anzahl": pd.Series(
                [element[1] for element in participant_list],
                [element[0] for element in participant_list],
            )
        }
    )
    return data


print(jonas())
for repetition in range(50):
    start = time.time()
    test = finn()
    finn_zeiten.append(time.time() - start)

    start = time.time()
    test = jonas()
    jonas_zeiten.append(time.time() - start)

finn_stats = np.array(finn_zeiten)
jonas_stats = np.array(jonas_zeiten)
print("Finn: ")
print(
    f"Mean: {np.mean(finn_stats)}  Min: {np.min(finn_stats)}   Max: {np.max(finn_stats)}"
)
print("Jonas: ")
print(
    f"Mean: {np.mean(jonas_stats)}  Min: {np.min(jonas_stats)}   Max: {np.max(jonas_stats)}"
)
"""
        participant_dataframe = pd.DataFrame(
            self.participant_list, columns=["date", "number"]
        )
        self.participant_dataframe = participant_dataframe.set_index(
            "date", drop=True, append=False
        )


anzahl = pd.Series([element[1] for element in teilnehmeranzahl], [element[0] for element in teilnehmeranzahl])
data = pd.DataFrame({'anzahl': anzahl})

finn:
round(100 * (data[day + 1, 1] / data[day, 1] - 1))


Bode:
lost_percentage = (1-(list[i][1]/list[i-1][1]))*100

chris:
perc_lost = (self.teilnehmer[i-1][1] - today) * 100 / today)
https://www.mathelounge.de/5437/prozentualen-verlust-berechnen-startkapital-euro-ende-tages


for n in range(len(data['anzahl'])):
        if pd.isna(data['anzahl'][n]):
            data['anzahl'][n] = data['anzahl'][n-1]*(1-(mean/100))

"""
