from graphics_and_games_klassen import *
from model import *
from view import * 
import keyboard

class CONTROLLER(EREIGNISBEHANDLUNG):
    def __init__(self): 
        super().__init__()
        self.gametick = 0
        self.v = VIEW()
        self.m = MODEL()
        self.enemy1 = self.m.ENEMY()
        self.bullets = []
        self.enemyBullets = []
        super().TaktdauerSetzen(4)

    def AktionAusfuehren(self):
      self.EnemyShooting()
      self.gametick += 1
      self.enemy1.MoveEnemy()
      self.v.ship.GanzNachHintenBringen()
      for bullet in self.bullets:
        if bullet.bullet.y <= -10:
          bullet.bullet.SichtbarkeitSetzen(False)
          self.bullets.remove(bullet)
        bullet.MoveBullet()
        print('Space pressed')
      for bullet1 in self.enemyBullets:
        bullet1.MoveEnemyBullet()
      
      
    def EnemyShooting(self):
       if len(self.enemyBullets) == 0:
          self.enemyBullets.append(self.m.BULLET(self.enemy1.enemy.x + 230, self.enemy1.enemy.y, "lila"))
       if self.enemyBullets[-1].bullet.y >= 300:
            self.enemyBullets.append(self.m.BULLET(self.enemy1.enemy.x + 230, self.enemy1.enemy.y, "lila")) 

    
    def TasteGedrueckt(self, taste):
        if taste == 'a':
          self.v.ship.Verschieben(-10, 0)
          self.v.hitBoxPlayer.PositionSetzen(self.v.ship.x + 10, self.v.ship.y + 25)
        if taste == 'd':
          self.v.ship.Verschieben(10, 0)
          self.v.hitBoxPlayer.PositionSetzen(self.v.ship.x, self.v.ship.y + 25)
        if keyboard.is_pressed(' '):
          self.bullets.append(self.m.BULLET(self.v.ship.x, self.v.ship.y, "schwarz"))


c = CONTROLLER()

