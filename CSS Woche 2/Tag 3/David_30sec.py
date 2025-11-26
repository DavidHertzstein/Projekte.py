import time
print("Willkommen zu meinem Quiz, du musst 10 Fragen beantworten, bis die Zeit abläuft.")
print("Lass uns das Spiel beginnen!!")
time.sleep(1)
print("Du hast 30 Sekunden Zeit!!")

frage1 = "Wie heißt die Hauptstadt von Frankreich? "
start = time.time()
antwort1 = input( frage1)
ende = time.time()
dauer1 = ende - start
if dauer1 > 30:
    print(f"Zeit abgelaufen!! Du hast {dauer1:.1f}  Sekunden gebraucht!")
    print("Game Over!!")
else:
    print(f"Du hast {dauer1:.1f} Sekunden gebraucht")

frage2 = "Was ist die witzigste Zahl aus Spongebob!! "
start2 = time.time()
antwort2 = int(input(frage2))
ende = time.time()
dauer2 = ende - start
if dauer2 > 30:
    print(f"Zeit abgelaufen!! Du hast {dauer2:.1f} Sekunden gebraucht!")
    print("Game Over!!")
else:
    print(f"Du hast {dauer2:.1f} Sekunden gebraucht")

frage3 = "Wie alt bist du? "
start = time.time()
antwort3 = int(input(frage3))
ende = time.time()
dauer3 = ende - start
if dauer3 > 30:
    print(f"Zeit abgelaufen!! Du hast {dauer3:.1f} Sekunden gebraucht!")
    print("Game Over!!")
else:
    print(f"Du hast {dauer3:.1f} Sekunden gebraucht")

frage4 = "Was ist 1+1? "
start = time.time()
antwort4 = int(input(frage4))
ende = time.time()
dauer4 = ende - start
if dauer4 > 30:
    print(f"Zeit abgelaufen!! Du hast {dauer4:.1f} Sekunden gebraucht!")
    print("Game Over!!")
else:
    print(f"Du hast {dauer4:.1f} Sekunden gebraucht")

frage5 = "20 * 30"
start = time.time()
antwort5 = int(input(frage5))
ende = time.time()
dauer5 = ende - start
if dauer5 > 30:
    print(f"Zeit abgelaufen!! Du hast {dauer5:.1f} Sekunden gebraucht!")
    print("Game Over!!")
else:
    print(f"Du hast {dauer5:.1f} Sekunden gebraucht")

frage6 = "Was ist die Wurzel aus 49? "
start = time.time()
antwort6 = int(input(frage6))
ende = time.time()
dauer6 = ende - start
if dauer6 > 30:
    print(f"Zeit abgelaufen!! Du hast {dauer6:.1f} Sekunden gebraucht!")
    print("Game Over!!")
else:
    print(f"Du hast {dauer6:.1f} Sekunden gebraucht")

frage7 = "Was ist das Gegenteil von hell? "
start = time.time()
antwort7 = input(frage7)
ende = time.time()
dauer7 = ende - start
if dauer7 > 30:
    print(f"Zeit abgelaufen!! Du hast {dauer7:.1f} Sekunden gebraucht!")
    print("Game Over!!")
else:
    print(f"Du hast {dauer7:.1f} Sekunden gebraucht")

frage8 = "Wie sieht diese ausgeschriebene Zahl als eine Ziffer aus \n viertausendzweihundertsechsunddreizig? "
start = time.time()
antwort8 = int(input(frage8))
ende = time.time()
dauer8 = ende - start
if dauer8 > 30:
    print(f"Zeit abgelaufen!! Du hast {dauer8:.1f} Sekunden gebraucht!")
    print("Game Over!!")
else:
    print(f"Du hast {dauer8:.1f} Sekunden gebraucht")

frage9 = "Wie heißt die Landeshauptstadt von Hessen? "
start = time.time()
antwort9 = input(frage9) 
ende = time.time()
dauer9 = ende - start
if dauer9 > 30:
    print(f"Zeit abgelaufen!! Du hast {dauer9:.1f} Sekunden gebraucht!")
    print("Game Over!!")
else:
    print(f"Du hast {dauer9:.1f} Sekunden gebraucht")

frage10 = "100 : 50? "
start = time.time()
antwort10 = int(input(frage10))
ende = time.time()
dauer10 = ende - start
if dauer10 > 30:
    print(f"Zeit abgelaufen!! Du hast {dauer10:.1f} Sekunden gebraucht!")
    print("Game Over!!")
else:
    print(f"Du hast {dauer10:.1f} Sekunden gebraucht")


if frage1.lower() == "Paris":
    print("Richtig!! Nächste Frage: ")  
 
elif frage2 == 24:
    print("Richtig!! Nächste Frage: ")
elif frage4 == 2:
    print("Richtig!! Nächste Frage: ")
elif frage5 == 600:
    print("Richtig!! Nächste Frage: ")
elif frage6 == 7:
    print("Richtig!! Nächste Frage: ")
elif frage7.lower == "dunkel":
    print("Richtig!! Nächste Frage: ")
elif frage8.lower == "Wiesbaden":
    print("Richtig!! Nächste Frage: ")
elif frage9 == 2:
    print("Richtig!! Nächste Frage: ")
elif frage10 == 2:
    print("Richtig!! Herzlichen Glückwunsch!! Du hast es geschafft!!")
else:
    print("Falsch")
    

