secret = "1537"
anzahl = 0
anzahlf = 0
raten = ""
while not raten == secret:
  raten = input('Errate die vierstellige Ziffer: ')

  for i in range(4):
    
    if secret[i] == raten[i]:
      #print( 'Die ' + str(i+1) +'. Ziffer ist korrekt!')
      anzahl = anzahl + 1
    elif not -1 == secret.find(raten[i]):
      #print ('Die ' + str(raten[i]) +'. Ziffer ist in den Secret, aber an der falschen Stelle!')
      anzahlf = anzahlf + 1

  if not anzahl == 0:     
    print(str(anzahl) + " Ziffern sind richtig.") 
    
  if not anzahlf == 0:
    print(str(anzahlf) + " Ziffern sind richtig ABER an der falschen Stelle!")

  if anzahlf == 0 and anzahl == 0:
    print('Alle Ziffern sind falsch!')

  anzahlf = 0
  anzahl = 0
 
print("Du hast es erratten!")