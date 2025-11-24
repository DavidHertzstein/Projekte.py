import random
wuerfelZahl = random.randint(1,6)
zaehler = 0
anzahlZaehler = 0
while zaehler < 30:
    print("Anzahl:",anzahlZaehler)
    print(wuerfelZahl)
    wuerfelZahl = random.randint(1,6)
    anzahlZaehler += 1
    
