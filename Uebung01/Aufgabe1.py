class Geburtstag:
    def print(self, d, m, y):
        print(str(d) + "." + str(m) + "." + str(y))

    def nice_print(self, d, m, y):
        switcher = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        }
        print(str(d) + ". " + switcher[m] + " " + str(y))


g = Geburtstag()

g.print(1, 1, 1999)
g.nice_print(1, 11, 1999)
