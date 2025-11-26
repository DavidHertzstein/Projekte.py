import webbrowser
#def webseite():
fehlerpunkte = 0
adresse1 = "https://www.google.com"
adresse2 = "https://www.bing.com"
adresse3 = "https://www.youtube.com"
print("Willkommen zu Browserlinks!! Sie können 3 Webseiten aufsuchen: Google, Bing und Youtube.")


while fehlerpunkte < 3:
    schreiben = input("Geben Sie eine Adresse ein: ")
    if schreiben.lower() == "google":
        suchmaschine = webbrowser.open(adresse1)
    elif schreiben.lower() == "bing":
        suchmaschine = webbrowser.open(adresse2)
    elif schreiben.lower() == "youtube":
        suchmaschine = webbrowser.open(adresse3)
    else:
        print("Das ist doch keine Webseite!!")
        fehlerpunkte += 1
        print("Versuche es nochmal!!")

    if fehlerpunkte == 3:
        print("Zu viele falsche Eingaben!! Internet-Zugriff wird blockiert!!")
        break
        


    
#adresse1 = "https://www.google.com"
#adresse2 = "https://www.bing.com"
#adresse3 = "https://www.youtube.com"
#eingabe = input("gebe eine Adresse ein ")

#if eingabe.lower() == "google":
    #suchmaschine = webbrowser.open_new_tab(adresse1)
#elif eingabe.lower() == "bing":
    #suchmaschine = webbrowser.open_new_tab(adresse2)
#elif eingabe.lower() == "youtube":
    #suchmaschine = webbrowser.open_new_tab(adresse3)
#else:
    #print("Das ist doch keine Webseite!!")




        
        
        








