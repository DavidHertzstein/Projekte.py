import webbrowser
import time

zaehler = 0
minuten = 0
fachmathe = "Mathe"
fachdeutsch = "Deutsch"
fachenglisch = "Englisch" 
print("Willkommen zu deinem eigenen Work-Life-Balance!! \n Du kannst Deutsch, Mathe und Englisch auswählen!!")
while zaehler < 8:
    if minuten == 0:
        
        if minuten < 90:
            eingabe2 = input("Welches Fach willst du lernen? ")
            if eingabe2.lower() == "mathe":
                print(f"lerne: {fachmathe}")
                time.sleep(10)
                minuten += 90
            elif eingabe2.lower() == "deutsch":
                print(f"lerne: {fachdeutsch}")
                time.sleep(10)
                minuten += 90
            elif eingabe2.lower() == "englisch":
                print(f"lerne: {fachenglisch}")
                time.sleep(10)
                minuten +=90
            elif eingabe2.lower() == "nichts":
                break
            else:
                print("Das ist doch kein Fach!!! ")
                zaehler +=1
                if zaehler == 8:
                    print("Du willst nicht lernen, du fauler Mensch!!")
                    break

            #print(f"Lerne: {eingabe2} ")
            #minuten += 90
            
            
    elif minuten == 90:
        print("Mach eine Pause!!! Ich bring dich zu deinem Liebllingssong")
        time.sleep(10)
        pause = webbrowser.open("https://www.youtube.com/watch?v=ho_UFEJgD08&list=RDho_UFEJgD08&start_radio=1")
        time.sleep(84)
        print("Pause vorbei!!")
        zaehler += 1
        if zaehler == 8:
            print("Programm wird beendet!!")
            break

        eingabe = input("willst du weiter lernen? ja oder nein? ")
        if eingabe.lower() == "ja":
            minuten = minuten - 90
        else:
            break
        
       










