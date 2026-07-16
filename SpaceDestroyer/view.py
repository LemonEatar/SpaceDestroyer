from graphics_and_games_klassen import *
import random 
import time

class VIEW(EREIGNISBEHANDLUNG):

    def __init__(self):
        super().__init__()
        self.bg = RECHTECK()
        self.bg.FarbeSetzen("schwarz")
        self.bg.PositionSetzen(-50,-50)
        self.bg.GroesseSetzen(0, 0)
        self.score = 0
        self.killcount = TEXT()
        self.killcount.PositionSetzen(10, 40)
        self.killcount.TextGroesseSetzen(20)
        self.killcount.TextSetzen(self.score)
        self.gameoverstate = TEXT()
        self.gameoverstate.FarbeSetzen("rot")
        self.gameoverstate.SichtbarkeitSetzen(False)
        #Raumschiff
        self.ship = DREIECK()
        self.lives = 100
        self.ship.PositionSetzen(500, 500)
        self.ship.GroesseSetzen(50, 100)
        self.gameoverstate.TextSetzen(self.lives)
        self.gameoverstate.TextGroesseSetzen(20)
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
               self.bg = RECHTECK()
               self.bg.FarbeSetzen("schwarz")
               self.bg.PositionSetzen(-50,-50)
               self.bg.GroesseSetzen(3000, 3000)
               self.gameoverstate.GanzNachVornBringen()
               self.gameoverstate.SichtbarkeitSetzen(True)
               self.gameoverstate.TextGroesseSetzen(100)
               self.gameoverstate.TextSetzen("Game Over")
               self.__del__()
