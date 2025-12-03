import pygame
import time
import sys
import random
from hero import Hero
from enemy import Enemies, Boss
 
 
def langsamer_text(text, delay=0.03):
    """Gibt Text langsam aus für dramatischen Effekt"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
 
def main_menu():
    """Hauptmenü des Spiels"""
    pygame.mixer.music.load("Projekt/mixkit-tapis-615.mp3")
    pygame.mixer.music.play(-1)
   
    while True:
        print("====================================================================")
        print("                         BLOOD HUNT")
        print("                  GARDENS OF BLOOD AND ROSES")
        print("====================================================================")
        print("1. Starten")
        print("2. Anleitung")
        print("3. Beenden")
        print("====================================================================")
 
        wahl = input("Wähle eine Option aus von (1-3): ")
       
        if wahl == "1":
            starte_spiel()
            break
        elif wahl == "2":
            anleitung()
        elif wahl == "3":
            langsamer_text("Spiel wird beendet!!")
            pygame.quit()
            sys.exit()
        else:
            print("Ungültige Angabe")
 
def anleitung():
    """Zeigt die Spielanleitung"""
    print("\n=== Anleitung ===\n")
    print("- Kämpfe gegen Gegner.")
    print("- Sammle Items")
    print("- Besiege die Rosenkönigin")
    print()
    input("Drücke ENTER-Taste für zurück.\n")
 
def starte_spiel():
    """Startet das Spiel mit der Story-Einführung"""
    pygame.mixer.music.stop()
    langsamer_text("Aria... einst eine friedliche Stadt voller Musik und Blumen.")
    langsamer_text("Doch diese Zeiten sind vorbei.")
    langsamer_text("Ein süßer, unheilvoller Rosenduft liegt über den Straßen.")
    langsamer_text("Menschen verschwinden und wer zurückkehrt, ist von Dornen umhüllt.")
    langsamer_text("Die Finstere Rosenkönigin Rosamira hat ihr Dornenschloss über das Land ausgebreitet.")
    langsamer_text("Lebende Ranken wuchern durch die Stadt, verwandeln Menschen in Kreaturen.")
    langsamer_text("\nDu bist der letzte Überlebende")
    langsamer_text("\nDeine Mission:")
    langsamer_text(" - Die Stadt Aria retten")
    langsamer_text(" - Die Dornen vernichten")
    langsamer_text(" - Die Rosenkönigin töten\n")
    langsamer_text("Das Schicksal der Menschheit liegt in deinen Händen... Bitte... \nrette uns...\n")
    charakterauswahl()
 
def charakterauswahl():
    """Lässt den Spieler seinen Charakter wählen"""
    pygame.mixer.music.load("Projekt-Tag/intense-rain-city-night-171461.mp3")
    pygame.mixer.music.play(-1)
   
    langsamer_text("Du bist da... Du siehst nichts...")
    langsamer_text("Das Einzige was du hörst, ist der Klang des Regens..")
    langsamer_text("Du weißt nicht mehr wer du bist..")
    langsamer_text("Doch du kannst dich erinnern was du bist..")
   
    # Charakterklasse wählen
    while True:
        charakterwahl = input("Also was bist du?? Gib ein (Krieger, Magier, Assasine): ").strip()
        if charakterwahl.lower() in ["krieger", "magier", "assasine"]:
            break
        print("Ungültige Klasse! Wähle: Krieger, Magier oder Assasine")
   
    # Held erstellen 
    held = Hero(name="Held", klasse=charakterwahl)
   
    langsamer_text(f"So mein {charakterwahl}, WACH AUF!!!!")
    langsamer_text(f"\nDeine Werte:")
    langsamer_text(f"HP: {held.hitpoints}")
    langsamer_text(f"Stärke: {held.strength}\n")
   
    stage3(held)
 
def kampf(held, gegner):
    """Führt einen Kampf zwischen Held und Gegner durch"""
    langsamer_text(f"\nEin {gegner.name} erscheint!")
 
    while held.hitpoints > 0 and gegner.hitpoints > 0:
        print(f"\n{'='*50}")
        print(f"{held.name} ({held.klasse}) HP: {held.hitpoints}/{held.maxhp}")
        print(f"{gegner.name} HP: {gegner.hitpoints}/{gegner.maxhp}")
        print(f"{'='*50}")
 
        zug = input("\n(1) Angreifen, (2) Heilen: ")
 
        if zug == "1":
            schaden = held.strength
            gegner.hitpoints -= schaden
            langsamer_text(f"Du triffst den Gegner und verursachst {schaden} Schaden!!")
           
        elif zug == "2":
            heilung = 25
            alter_hp = held.hitpoints
            held.hitpoints += heilung
            if held.hitpoints > held.maxhp:
                held.hitpoints = held.maxhp
            tatsaechliche_heilung = held.hitpoints - alter_hp
            langsamer_text(f"Du heilst dich um {tatsaechliche_heilung} HP!")
           
        else:
            langsamer_text(f"Ungültige Angabe! {gegner.name} erhält einen freien Angriff!")
 
        # Gegner besiegt?
        if gegner.hitpoints <= 0:
            langsamer_text(f"\n*** Du hast {gegner.name} besiegt! ***\n")
            return True
       
        # Gegner greift an
        gegner_schaden = gegner.strength
        held.hitpoints -= gegner_schaden
        langsamer_text(f"Der {gegner.name} trifft dich. Du erleidest {gegner_schaden} Schaden!")
 
    # Held gestorben?
    if held.hitpoints <= 0:
        langsamer_text("\n*** Du wurdest besiegt! ***")
        return False
   
    return True
 
def stage3(held):
    """Das Wellensystem - 10 Wellen mit Gegnern"""
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Projekt/Stage3 music.mp3")
    pygame.mixer.music.play(-1)
 
    langsamer_text("\nDu steigst die Treppen hinauf..")
    langsamer_text("Als du oben angekommen bist, bemerkst du, dass du")
    langsamer_text("in die Gemächer der Königin gelangt bist.")
    langsamer_text("Dein Ziel ist ganz nah, gib nicht auf!!!!\n")
   
    aktuelleWelle = 1
 
    while aktuelleWelle <= 10:
        langsamer_text(f"\n{'*'*50}")
        langsamer_text(f"*** WELLE {aktuelleWelle} BEGINNT ***")
        langsamer_text(f"{'*'*50}")
 
        # Welle 9: Miniboss
        if aktuelleWelle == 9:
            miniboss = Boss()  
            miniboss.enemy_schwarzer_ritter()
           
            langsamer_text("\n" + "="*60)
            langsamer_text("Ein schwarzer Ritter erscheint vor dem Tor")
            langsamer_text("der Rosenkönigin!")
            langsamer_text("="*60)
            langsamer_text('"Du bist weit gekommen, Held..."')
            langsamer_text('"Aber hier endet dein Weg!!"')
            langsamer_text('"Ich lasse nicht zu, dass du meine Rosenkönigin tötest!!"\n')
           
            erfolgreich = kampf(held, miniboss)
       
        # Normale Wellen: Zufallsgegner
        else:
            gegner = Enemies()
            zufallgegner = random.choice([1, 2, 3])
           
            if zufallgegner == 1:
                gegner.enemy_goblin()
            elif zufallgegner == 2:
                gegner.enemy_orc()
            else:
                gegner.enemy_stonegolem()
           
            erfolgreich = kampf(held, gegner)
 
        # Held gestorben?
        if not erfolgreich:
            langsamer_text("\nDu bist gefallen...")
            langsamer_text("GAME OVER")
            return False
       
        # Welle überlebt!
        langsamer_text(f"\n*** Welle {aktuelleWelle} überlebt! ***")
       
        # Kleine Heilung nach jeder Welle
        if aktuelleWelle < 10:
            held.hitpoints += 20
            if held.hitpoints > held.maxhp:
                held.hitpoints = held.maxhp
            langsamer_text(f"Du hast dich etwas erholt! HP: {held.hitpoints}/{held.maxhp}\n")
       
        aktuelleWelle += 1
 
    # Alle Wellen überlebt!
    langsamer_text("\n" + "="*60)
    langsamer_text("*** DU HAST ALLE 10 WELLEN ÜBERLEBT! ***")
    langsamer_text("="*60)
    langsamer_text("Der Weg zur Rosenkönigin ist frei...")
    langsamer_text("TO BE CONTINUED...")
    return True
 
# Spiel starten
if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    main_menu()

