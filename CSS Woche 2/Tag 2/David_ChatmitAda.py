def nameinput(name2):
    return name2
#Das was du im input eingibst wird als Rückgabewert für die Variable name2 gespeichert.
def alterinput(alter):
    return alter
#Das was du im input eingibst wird als Rückgabewert für die Variable name2 gespeichert.

name1 = "Ada"
name3 = "Unbekannt"
alter2 = 20




print(name3+": Ein schönen guten Tag, wie heißt du?")

name2 = input("Gib deinen Namen ein: ")


print(name2+": Mein Name ist "+name2+" und wie heißt du??")

print(name1+": Hi",name2,"mein Name ist",name1,"Freut mich dich kennen zu lernen!!")

print(name2+": Hi",name1,"Freut mich auch dich kennen zu lernen!! Wie alt bist du??<" )

print(name1+": Ich bin",alter2,"Jahre alt. Und wie alt bist du?")

alter = int(input("Gib deinen Alter ein: "))

print(name2+": Ich bin",alter,"Jahre alt.")
if alter < 18:
    print(name1+": Oh, du bist ja minderjährig, dann musst du zum Weicheischuppen-Junior. Ach was ich mach nur Spaß. :)")
elif alter >= 18:
    print(name1+": Wow du bist echt ein alter Hase!! Ich bin sogar jünger als du ahahah!! Ich mach nur Spaß")

print(name2+": Hahahahha, ne alles gut kann ich verstehen. XD")

print(name1+": Aber gut jetzt muss ich dir eine sehr wichtige Frage stellen. Es geht dabei über Leben und Tod")

print(name2+": Oh! Okay, dann bin ich mal gespannt schieß los!!")

print(name1+": Magst du Animes?????")

ja =input("Tippe ja oder nein: ")

if ja == "ja":
    print(name1+": Wow, wie schön endlich ein Gleichgesinnter.")

else:
    print(name1+": Oh... das musst du aber dringend nachholen!! :)")
    
print(name1 +": Aber gut ich verabschiede mich jetzt. Ich wünsche dir einen schönen Tag, aufwiedersehen", name2)

print(name2 +": Aufwiedersehen,",name1,":)")

