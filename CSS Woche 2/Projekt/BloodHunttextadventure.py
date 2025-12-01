import sys
import time
import pygame

def langsamer_text(text, delay = 0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def main_menu():
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
        if wahl == ("1"):
            starte_spiel()
        elif wahl == ("2"):
            anleitung()
        elif wahl == ("3"):
            langsamer_text("Spiel wird beendet!!")
            pygame.quit()
            sys.exit()
        else:
            print("ungültige Angabe")

def anleitung():
    print("\n=== Anleitung ===\n")
    print("-Kämpfe gegen Gegner.")
    print("-Sammle Items")
    print("-Besiege die Rosenkönigin")
    print()
    input("Drücke ENTER-Taste für zurück. \n")


def starte_spiel():
    pygame.mixer.music.stop()
    langsamer_text("Aria... einst eine friedliche Stadt voller Musik und Blumen.")
    langsamer_text("Doch diese Zeiten sind vorbei.")
    langsamer_text("Ein süßer, unheilvoller Rosenduft liegt über den Straßen.")
    langsamer_text("Menschen verschwinden – und wer zurückkehrt, ist von Dornen umhüllt.")
    langsamer_text("Die Finstere Rosenkönigin hat ihr Dornenschloss über das Land ausgebreitet.")
    langsamer_text("Lebende Ranken wuchern durch die Stadt, verwandeln Menschen in Kreaturen.")
    langsamer_text("\nDu bist einer der letzten, die noch frei sind.")
    langsamer_text("Dein Amulett schützt dich – doch nicht für immer.")
    langsamer_text("\nDeine Mission:")
    langsamer_text(" - Die Stadt Aria retten")
    langsamer_text(" - Die Dornen vernichten")
    langsamer_text(" - Die Rosenkönigin töten\n")
    langsamer_text("Das Schicksal der Menschheit liegt in deinen Händen...\n")


def vor_Dem_tor():
   langsamer_text("Aria... einst eine friedliche Stadt voller Musik und Blumen.")
   langsamer_text("Doch diese Zeiten sind vorbei.")
   langsamer_text("Ein süßer, unheilvoller Rosenduft liegt über den Straßen.")
   langsamer_text("Menschen verschwinden – und wer zurückkehrt, ist von Dornen umhüllt.")
   langsamer_text("Die Finstere Rosenkönigin hat ihr Dornenschloss über das Land ausgebreitet.")
   langsamer_text("Lebende Ranken wuchern durch die Stadt, verwandeln Menschen in Kreaturen.")
   langsamer_text("\nDu bist einer der letzten, die noch frei sind.")
   langsamer_text("Dein Amulett schützt dich – doch nicht für immer.")
   langsamer_text("\nDeine Mission:")
   langsamer_text(" - Die Stadt Aria retten")
   langsamer_text(" - Die Dornen vernichten")
   langsamer_text(" - Die Rosenkönigin töten\n")
   langsamer_text("Das Schicksal der Menschheit liegt in deinen Händen...\n")
   
   langsamer_text("Du stehst im Foyer...")


pygame.init()
pygame.mixer.init()
main_menu()
     