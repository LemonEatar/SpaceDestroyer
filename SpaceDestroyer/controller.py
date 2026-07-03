from graphics_and_games_klassen import *
from model import *
from view import * 
import keyboard

class CONTROLLER(EREIGNISBEHANDLUNG):
    def __init__(self): 
        super().__init__()
        self.v = VIEW()
        self.m = MODEL()
        self.enemy1 = self.m.ENEMY()
        self.bullets = []
        super().TaktdauerSetzen(4)

    #def TaktdauerSetzen(self, ms):
       #return super().TaktdauerSetzen(ms)

    def AktionAusfuehren(self):
       self.enemy1.MoveEnemy()
       self.v.ship.GanzNachHintenBringen()
       for bullet in self.bullets:
        bullet.MoveBullet()
        print('Space pressed')


    
    def TasteGedrueckt(self, taste):
        if taste == 'a':
          self.v.ship.Verschieben(-10, 0)
          self.v.hitBoxPlayer.PositionSetzen(self.v.ship.x + 10, self.v.ship.y + 25)
        if taste == 'd':
          self.v.ship.Verschieben(10, 0)
          self.v.hitBoxPlayer.PositionSetzen(self.v.ship.x, self.v.ship.y + 25)
        if keyboard.is_pressed(' '):
          self.bullets.append(self.m.BULLET(self.v.ship.x, self.v.ship.y))


c = CONTROLLER()
