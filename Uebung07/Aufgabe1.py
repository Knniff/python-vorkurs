import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math


class ParticipantData:
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
    participant_dataframe = None
    participant_array = None

    def __init__(self):
        # 1.b)
        self.participant_array = np.array(self.participant_list)
        # 1.d)
        participant_dataframe = pd.DataFrame(
            self.participant_list, columns=["date", "number"]
        )
        self.participant_dataframe = participant_dataframe.set_index(
            "date", drop=True, append=False
        )

    # 1.f)
    def extrapolate(self):
        data = self.participant_array
        prediction_list = []
        loss = self.loss_data()[2]
        for day in range(len(data)):
            if data[day, 1] == None:
                data[day, 1] = data[day - 1, 1] - loss
                prediction_list.append((data[day, 0], int(data[day, 1])))
        prediction_dataframe = pd.DataFrame(
            prediction_list, columns=["date", "prediction"]
        )
        merge = self.participant_dataframe.join(
            prediction_dataframe.set_index("date", drop=True, append=False)
        )
        for day in range(len(merge["number"])):
            if np.isnan(merge["number"][day]):
                merge["number"][day] = 0
        for day in range(len(merge["prediction"])):
            if np.isnan(merge["prediction"][day]):
                merge["prediction"][day] = 0
        return merge

    # 1.e / 1.g)
    def make_plot(self, data):
        data.plot.barh(title="Participants in the Lecture")
        plt.savefig("test.png")

    def daily_lost(self):
        data = self.participant_array
        percentage_list = []
        for day in range(len(data) - 1):
            if data[day, 1] != None and data[day + 1, 1] != None:
                percentage_list.append(100 * (1 - data[day + 1, 1] / data[day, 1]))
        print("1.a)Daily Loss: ")
        print(percentage_list)

    def loss_data(self):
        data = self.participant_array
        loss_list = []
        for day in range(len(data) - 1):
            if data[day, 1] != None and data[day + 1, 1] != None:
                loss_list.append(data[day, 1] - data[day + 1, 1])
        info = (np.min(loss_list), np.max(loss_list), round(np.mean(loss_list)))
        return info


gen1 = ParticipantData()
gen1.daily_lost()
info = gen1.loss_data()
print("1.c) Loss-Info: ")
print(f"Min: {info[0]}")
print(f"Max: {info[1]}")
print(f"Mean: {info[2]}")
gen1.make_plot(gen1.extrapolate())
