from typing import List, Dict
import time

# 'ampel' -> {'a': 1, 'm': 1, 'p': 1, 'e': 1, 'l': 1}
def zaehlen(wort: str) -> Dict[str, int]:

    return {buchstabe: wort.count(buchstabe) for buchstabe in wort}


def anagramm(startwort: str) -> List[str]:
    startwort = startwort.upper()
    anagramme = []

    with open(
        "/home/knniff/python-projects/python-vorkurs/Uebung08/word_list.txt", "r"
    ) as file:
        wortliste = file.readlines()
        z_start = zaehlen(startwort)

        # Löscht Zeilenumbrüche in jedem Wort
        for stelle, wort in enumerate(wortliste):
            wort = wort.replace("\n", "")
            wortliste[stelle] = wort

        # Erstellt wort_dict. Jedes Wort ist eine Schlüssel und
        # zeigt auf die jeweiligen Anzahlen von Buchstaben
        # wort_dict = {}
        # for wort in wortliste:
        #     if len(wort) == len(startwort):
        #        wort_dict[wort] = zaehlen(wort)

        for wort in wortliste:
            if len(wort) == len(startwort):
                passt = True
                for char in wort:
                    if char not in startwort:
                        passt = False
                        break
                    else:
                        if wort.count(char) != z_start[char]:
                            passt = False
                            break

                if passt:
                    anagramme.append(wort)

    return anagramme


times = []
for a in range(50):
    start = time.time()
    print(anagramm("ampel"))
    times.append(time.time() - start)

print(sum(times) / 50)