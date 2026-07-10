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
        self.enemies = []
        self.bullets = []
        self.left = True
        self.boss = self.m.ENEMY()
        #self.boss.PositionSetzen(-200, 50)
        self.enemyBullets = []
        self.bossBullets = []
        super().TaktdauerSetzen(4)

    def AktionAusfuehren(self):

      if self.v.ship.x < 0:
         self.left = False
      elif self.v.ship.x >= 800:
         self.left = True
      for enemy1 in self.enemies:
         enemy1.isHit()
         self.EnemyShooting(enemy1)
         if enemy1.zustand == 1:
          enemy1.MoveEnemy()
         if enemy1.zustand == 0:
          self.boss.MoveEnemy()
          self.BossShooting()
      self.v.movePlayer(self.left)
      self.gametick += 0.5
      
      self.v.ship.GanzNachHintenBringen()
      for bullet in self.bullets:
        if bullet.bullet.y <= -10:
          bullet.bullet.SichtbarkeitSetzen(False)
          self.bullets.remove(bullet)
        bullet.MoveBullet()
      for bullet1 in self.enemyBullets:
        self.v.playerIsHit(bullet1.ebullet.x, bullet1.ebullet.y)
        bullet1.MoveEnemyBullet()
    ##  if self.enemy1.zustand == 0:
      #   self.boss.MoveEnemy()
     #    for bullet2 in self.bossBullets:
      #      bullet2.MoveBossBullet()
      
      
    def EnemyShooting(self, enemy1):
       if len(self.enemyBullets) == 0:
          self.enemyBullets.append(enemy1.createEBullet())
       if self.enemyBullets[-1].ebullet.y >= 500:
            self.enemyBullets.append(enemy1.createEBullet()) 
          
    def BossShooting(self):
       if len(self.bossBullets) == 0:
          self.bossBullets.append(self.m.BOSSBULLET(self.boss.enemy.x + 230, self.boss.enemy.y + 10))
       if self.bossBullets[-1].bossbullet.y >= 500:
          self.bossBullets.append(self.m.BOSSBULLET(self.boss.enemy.x + 230, self.boss.enemy.y + 10))

    
    def TasteGedrueckt(self, taste):
        if taste == 'a':
          self.left = True
        if taste == 'd':
           self.left = False
        if keyboard.is_pressed(' '):
          self.bullets.append(self.m.BULLET(self.v.ship.x, self.v.ship.y))
    def createEnemy(self):
       self.enemies.append(self.m.ENEMY())


c = CONTROLLER()
c.createEnemy()
