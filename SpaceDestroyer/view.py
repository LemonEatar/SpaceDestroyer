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
    
    def movePlayer(self, taste):
       
    class BULLET(EREIGNISBEHANDLUNG):

        def __init__(self, x, y):
            super().__init__()
            self.bullet = DREIECK()
            self.bullet.PositionSetzen(x, y)
            self.bullet.GroesseSetzen(5,15)
            self.bullet.FarbeSetzen("schwarz")

        def AktionAusfuehren(self):
            print("executed")
            self.bullet.PositionSetzen(self.bullet.x, self.bullet.y-1)
        def TaktdauerSetzen(self, ms):
            return super().TaktdauerSetzen(ms)
        
    class ENEMY(FIGUR):
        
        def __init__(self):
            super().__init__()
            self.FigurteilFestlegenEllipse(500, 50, 80, 80, "grün")

        def AktionAusfuehren(self):
            self.Drehen(random.randint(0,360))
            self.Gehen(random.randint(1,30))
