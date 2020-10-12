secret = "1537"
anzahl = 0
anzahlf = 0
raten = ""
found = "" #will contain the positions of found numbers, to make sure that one number isn't found twice
while not raten == secret:
  raten = input('Errate die vierstellige Ziffer: ')

  for i in range(4):
    
    if secret[i] == raten[i]:
      #print( 'Die ' + str(i+1) +'. Ziffer ist korrekt!')
      anzahl = anzahl + 1

      #decreating half correct counter in the case that a number was "found" at the wrong spot
      #but later found in the right spot -> right spot is more important that false spot
      if str(i) in found: 
        anzahlf -= 1

      found += str(i) #strorring number at this position was found

                                              #checking that this position wasn't found earlier
    elif not -1 == secret.find(raten[i]) and str(secret.find(raten[i])) not in found:
      #print ('Die ' + str(raten[i]) +'. Ziffer ist in den Secret, aber an der falschen Stelle!')
      anzahlf = anzahlf + 1
      found += str(secret.find(raten[i])) #strorring number at this position was found

  if not anzahl == 0:     
    print(str(anzahl) + " Ziffern sind richtig.") 
    
  if not anzahlf == 0:
    print(str(anzahlf) + " Ziffern sind richtig ABER an der falschen Stelle!")

  if anzahlf == 0 and anzahl == 0:
    print('Alle Ziffern sind falsch!')

  anzahlf = 0
  anzahl = 0
  found = ""
 
print("Du hast es erratten!")