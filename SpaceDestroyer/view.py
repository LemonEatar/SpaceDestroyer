from graphics_and_games_klassen import *

class VIEW(EREIGNISBEHANDLUNG):

    def __init__(self):
        super().__init__()
        self.ship = DREIECK()
        self.ship.PositionSetzen(500, 500)
        self.ship.GroesseSetzen(50, 100)
        self.bullet = DREIECK()
        self.bullet.SichtbarkeitSetzen(False)
        self.bullet.GroesseSetzen(5,15)
        self.bullet.FarbeSetzen("schwarz")

