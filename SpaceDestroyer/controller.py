from graphics_and_games_klassen import *
from model import *
from view import * 
import keyboard

class CONTROLLER(EREIGNISBEHANDLUNG):
    def __init__(self): 
        super().__init__()
        self.gametick = 0
        # MVC Imports
        self.v = VIEW()
        self.m = MODEL()
        # List of enteties to handle multiple Bullets / Enemys
        self.enemies = []
        self.bullets = []
        self.enemyBullets = []
        self.bossBullets = []
        # Variables
        self.left = True
        self.fixedEnemyCount = 0
        self.boss = self.m.BOSS()
        self.boss.enemy.SichtbarkeitSetzen(False)

        super().TaktdauerSetzen(4)

    def AktionAusfuehren(self):
      self.gametick += 0.5
      # Enemy Spawn
      if self.gametick % 100 == 0 and self.fixedEnemyCount <= 5:
         self.fixedEnemyCount += 1
         print(self.fixedEnemyCount)
         self.createEnemy()
      # player movement
      if self.v.ship.x < 0:
         self.left = False
      elif self.v.ship.x >= 1200:
         self.left = True
      self.v.movePlayer(self.left) 
      # Enemy Collision detection and Shooting
      if len(self.enemies) > 0:
         for enemy1 in self.enemies:
            if enemy1.isHit() == True:
               self.enemies.remove(enemy1) 
         enemy1.MoveEnemy()
         self.EnemyShooting(enemy1)
      #if self.boss.isHit() == True:
     #    self.boss.enemy.Entfernen()
# Boss Spawn
      if self.fixedEnemyCount == 5 and len(self.enemies) == 0:
          self.boss.enemy.SichtbarkeitSetzen(True)
          self.boss.MoveBoss()
          self.BossShooting()
      self.v.ship.GanzNachHintenBringen()
# Bullet Movement
      for bullet in self.bullets:
        if bullet.bullet.y <= -10:
          bullet.bullet.SichtbarkeitSetzen(False)
          self.bullets.remove(bullet)
        bullet.MoveBullet()
      # Enemy Bullet Movement
      for bullet1 in self.enemyBullets:
        self.v.playerIsHit(bullet1.ebullet.x, bullet1.ebullet.y)
        bullet1.MoveEnemyBullet()
        if bullet1.ebullet.y >= 800:
            self.enemyBullets.remove(bullet1)
      # Boss Bullet Movement
      for bullet2 in self.bossBullets:
         self.v.playerIsHit(bullet2.bbullet.x, bullet2.bbullet.y)
         bullet2.MoveBossBullet()
         if bullet2.bbullet.y >= 800:
            self.bossBullets.remove(bullet2)
      # Player Death
      if self.v.lives <= 0:
         super().Anhalten()
    def EnemyShooting(self, enemy1):
       if len(self.enemyBullets) == 0:
          self.enemyBullets.append(enemy1.createEBullet())
       if self.enemyBullets[-1].ebullet.y >= 500:
            self.enemyBullets.append(enemy1.createEBullet()) 
          
    def BossShooting(self):
      if len(self.bossBullets) == 0:
          self.bossBullets.append(self.boss.createBossBullet())
      if self.bossBullets[-1].bbullet.y >= 500:
         self.bossBullets.append(self.boss.createBossBullet()) 
       


    
    def TasteGedrueckt(self, taste):
        if taste == 'a':
          self.left = True
        if taste == 'd':
           self.left = False
        if keyboard.is_pressed(' '):
          self.bullets.append(self.m.BULLET(self.v.ship.x, self.v.ship.y))
    def createEnemy(self):
       self.enemies.append(self.m.ENEMY())
       print("New Enemy")

c = CONTROLLER()
