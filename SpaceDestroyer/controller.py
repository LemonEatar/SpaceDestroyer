from graphics_and_games_klassen import *
from model import *
from view import * 
import keyboard

class CONTROLLER(EREIGNISBEHANDLUNG):
    def __init__(self): 
        super().__init__()
        self.v = VIEW()
        self.m = MODEL()
    def TasteGedrueckt(self, taste):
        if taste == 'a':
          self.v.ship.Verschieben(-10, 0)
          self.v.hitBoxPlayer.PositionSetzen(self.v.ship.x + 10, self.v.ship.y + 25)
        if taste == 'd':
          self.v.ship.Verschieben(10, 0)
          self.v.hitBoxPlayer.PositionSetzen(self.v.ship.x, self.v.ship.y + 25)
        if keyboard.is_pressed(' '):
          self.v.ship.GanzNachHintenBringen()
          bullet = self.v.BULLET(self.v.ship.x, self.v.ship.y)
          bullet.TaktdauerSetzen(4)
          print('Space pressed')
    def Enemy(self):
        enemy = self.v.ENEMY()
        enemy.TaktdauerSetzen(4)

c = CONTROLLER()
c.Enemy()
