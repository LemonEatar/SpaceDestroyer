from graphics_and_games_klassen import *
import random 

class VIEW(EREIGNISBEHANDLUNG):

    def __init__(self):
        super().__init__()
        self.gameoverbg = RECHTECK()
        self.gameoverbg.PositionSetzen(-100, -100)
        self.gameoverbg.FarbeSetzen("schwarz")
        self.gameoverbg.GroesseSetzen(2000, 2000)
        self.gameoverbg.SichtbarkeitSetzen(False)
        self.gameoverstate = TEXT()
        self.gameoverstate.TextGroesseSetzen(100)
        self.gameoverstate.SichtbarkeitSetzen(False)
        #Raumschiff
        self.ship = DREIECK()
        self.lives = 100
        self.ship.PositionSetzen(500, 500)
        self.ship.GroesseSetzen(50, 100)
        self.gameoverstate.TextSetzen(self.lives)
    def movePlayer(self, left):
        if left == True:
            self.ship.Verschieben(-1, 0)
        else:
            self.ship.Verschieben(1,0)
    def __del__(self):
        print("Player destroyed")
    def playerIsHit(self, ebulletx, ebullety):
        if self.ship.x + 10 > ebulletx > self.ship.x - 10 and ebullety >= self.ship.y:
           self.lives -= 1
           self.gameoverstate.TextSetzen(self.lives)
           if self.lives <= 0:
               self.gameoverbg.SichtbarkeitSetzen(True)
               self.gameoverstate.SichtbarkeitSetzen(True)
               self.gameoverstate.TextGroesseSetzen(250)
               self.gameoverstate.TextSetzen("Game Over")
               self.__del__
           print(self.lives)

