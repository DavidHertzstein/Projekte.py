class Enemies:
   def __init__(self):
       self.hitpoints = 100 #Aktuelle Anzahl der Lebenspunkte
       self.maxhp = 100 #Maximale Anzahl der Lebenspunkte
       self.strength = 10 #Stärke zeigt wie viel Schaden der Gegner macht
       self.dodgechance = 1 #Zeigt eine mögliche Ausweich-Chance 1 = 10% um auszuweichen, 4 = 40% etc
       self.critchance = 1 #Zeigt Chancen auf kritische Treffer 1 = 10% um auszuweichen, 4 = 40% etc
#<<<Enemy Goblin>>>
   def enemy_goblin(self):
       self.hitpoints = 100 #Aktuelle Anzahl der Lebenspunkte
       self.maxhp = 100 #Maximale Anzahl der Lebenspunkte
       self.name = "Goblin"
       self.strength = 10 #Stärke zeigt wie viel Schaden der Gegner macht
       self.dodgechance = 3 #Zeigt eine mögliche Ausweich-Chance 1 = 10% um auszuweichen, 4 = 40% etc
       self.critchance = 2 #Zeigt Chancen auf kritische Treffer 1 = 10% um auszuweichen, 4 = 40% etc
#<<<Enemy Orc>>>
   def enemy_orc(self):
       self.hitpoints = 100 #Aktuelle Anzahl der Lebenspunkte
       self.maxhp = 100 #Maximale Anzahl der Lebenspunkte
       self.name = "Orc"
       self.strength = 10 #Stärke zeigt wie viel Schaden der Gegner macht
       self.dodgechance = 1 #Zeigt eine mögliche Ausweich-Chance 1 = 10% um auszuweichen, 4 = 40% etc
       self.critchance = 1 #Zeigt Chancen auf kritische Treffer 1 = 10% um auszuweichen, 4 = 40% etc
#<<<Enemy Stone Golem>>>
   def enemy_stonegolem(self):
       self.hitpoints = 200 #Aktuelle Anzahl der Lebenspunkte
       self.maxhp = 200 #Maximale Anzahl der Lebenspunkte
       self.name = "Stone Golem"
       self.strength = 10 #Stärke zeigt wie viel Schaden der Gegner macht
       self.dodgechance = 0 #Zeigt eine mögliche Ausweich-Chance 1 = 10% um auszuweichen, 4 = 40% etc
       self.critchance = 1 #Zeigt Chancen auf kritische Treffer 1 = 10% um auszuweichen, 4 = 40% etc

   
    
