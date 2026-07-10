from graphics_and_games_klassen import *
import random 

class VIEW(EREIGNISBEHANDLUNG):

    def __init__(self):
        super().__init__()
        #Raumschiff
        self.ship = DREIECK()
        self.ship.PositionSetzen(500, 500)
        self.ship.GroesseSetzen(50, 100)
        self.hitBoxPlayer = FIGUR(self.ship.x, self.ship.y + 25, 90)
    def movePlayer(self, left):
        if left == True:
            self.ship.Verschieben(-1, 0)
        else:
            self.ship.Verschieben(1,0)
    def playerIsHit(self, ebulletx, ebullety):
        if self.ship.x + 10 > ebulletx > self.ship.x - 10 and ebullety >= self.ship.y:
            print("player is hit")
