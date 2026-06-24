from graphics_and_games_klassen import *
from model import *
from view import *

class CONTROLLER(EREIGNISBEHANDLUNG):
    def __init__(self): 
        super().__init__()
        self.v = VIEW()
        self.m = MODEL()
    def TasteGedrueckt(self, taste):
        if taste == "D":
            self.v.ship.WinkelSetzen(20)
c = CONTROLLER()
