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
    
    #def movePlayer(self, taste):
       
    class GAMELOOP(EREIGNISBEHANDLUNG):

        def __init__(self):
            super().__init__()
