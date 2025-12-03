class Hero:
    def __init__(self, name, klasse):  
        self.name = name
        self.klasse = klasse
        self.hitpoints = 100
        self.maxhp = 100
        self.strength = 20
 
        # Klassenspezifische Werte
        if self.klasse.lower() == "krieger":
            self.hitpoints = 120
            self.maxhp = 120
            self.strength = 25
        elif self.klasse.lower() == "magier":
            self.hitpoints = 80
            self.maxhp = 80
            self.strength = 30
        elif self.klasse.lower() == "assasine":
            self.hitpoints = 90
            self.maxhp = 90
            self.strength = 28
