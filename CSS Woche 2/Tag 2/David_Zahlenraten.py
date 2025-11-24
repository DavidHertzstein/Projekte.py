import random
zaehler = 0
name = "Captain Hook"
print(name+": Willkommen bei Captain Hook's Zahlenraten.")

print(name+": Ich habe eine Geheimzahl, kannst du meine Geheimzahl erraten? Du musst nur eine Zahl auswählen die von 1 bis 100 geht, wenn die Zahl richtig ist bekommst du ein Preis, wenn nicht landest du über der Planke!!!")
print(name+": Aber keine Sorge, du hast 6 Versuche bevor du unter gehst, also entscheide weise. LASST DAS SPIEL BEGINNEN!!")
while zaehler <= 7:
    errateZahl = int(input("Gebe eine Zahl ein: "))
    zaehler +=1
    print("Anzahl:",zaehler)
    print(errateZahl)
    
    if errateZahl == 24:
        print(name+": Herzlichen Glückwunsch!! Du gewinnst 1 Million Euro!")
        break
    elif errateZahl < 24:
        print(name+": Zu niedrig, du Landratte!")
    elif errateZahl > 24:
        print(name+": Zu hoch!")
    
    if zaehler == 6:
        print(name+": Game Over!!!")
        break
    elif zaehler == 3:
        print(name+": Ich gebe dir ein Tipp! Die Geheimzahl liegt ziwschen die Zahlen 10-30. Konzentriere dich!!!")
    elif zaehler == 5:
        print(name+": Ich gebe dir einen letzten Tipp!! Hast du Spongebob geschaut? Was ist die witzigste Zahl?? Tick-Tack-Tick-Tack")
        
    
    
    

    
    



