import random
wuerfelZahl = random.randint(1,6)
zaehler = 0
while zaehler < 30:
    print("Anzahl:",zaehler)
    print(wuerfelZahl)
    wuerfelZahl = random.randint(1,6)
    zaehler += 1
