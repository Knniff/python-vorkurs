secret = "1537"
anzahl = 0
anzahlf = 0
raten = ""
# will contain the positions of found numbers, to make sure that one number isn't found twice
found = ""
while not raten == secret:
    raten = input("Guess the secret: ")
    for i in range(4):

        if secret[i] == raten[i]:
            anzahl = anzahl + 1
            # decreasing half correct counter in the case that a number was "found" at the wrong spot
            # but later found in the right spot -> right spot is more important that false spot
            if str(i) in found:
                anzahlf -= 1
            # storing number at this position was found
            found += str(i)

        # checking that this position wasn't found earlier
        elif (
            not -1 == secret.find(raten[i]) and str(secret.find(raten[i])) not in found
        ):
            anzahlf = anzahlf + 1
            found += str(
                secret.find(raten[i])
            )  # storing number at this position was found

    if not anzahl == 0:
        print(str(anzahl) + "characters are right.")

    if not anzahlf == 0:
        print(str(anzahlf) + " characters are right BUT in the wrong position!")

    if anzahlf == 0 and anzahl == 0:
        print("All characters are wrong!")

    anzahlf = 0
    anzahl = 0
    found = ""

print("You guessed right!")
