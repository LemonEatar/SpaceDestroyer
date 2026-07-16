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
        self.message = TEXT(300, 300, 0, 50, "rot")
        self.message.PositionSetzen(0, 5000)

        super().TaktdauerSetzen(4)

    def AktionAusfuehren(self):
      self.gametick += 0.5
      # Enemy Spawn
      if self.gametick % 300 == 0 and self.fixedEnemyCount < 5 or self.gametick % 300 == 0 and self.boss.isAlive == False:
         self.fixedEnemyCount += 1
         print(self.fixedEnemyCount)
         self.createEnemy()

      # player movement
      if self.v.ship.x < 0:
         self.left = False
      elif self.v.ship.x >= 1200:
         self.left = True
      self.v.movePlayer(self.left)

      # Enemy collision detection, movement and shooting
      for enemy1 in self.enemies[:]:        # iterate over a COPY of the list
         if enemy1.isHit():
               self.enemies.remove(enemy1)
               self.v.score +=1
               self.v.killcount.TextSetzen(self.v.score)
               print("Enemy is Hit")
               continue                      # skip dead enemy, don't move/shoot it
         enemy1.MoveEnemy()
         self.EnemyShooting(enemy1)

      # Boss Spawn
      if self.fixedEnemyCount == 5 and len(self.enemies) == 0 and self.boss.enemy.y <= 500:
         self.boss.enemy.SichtbarkeitSetzen(True)
         self.boss.MoveBoss()
         self.BossShooting()

      # Boss Despawn
      if self.boss.isHit():
          self.boss.PositionSetzen(50, 3000)

      self.v.ship.GanzNachHintenBringen()

      if self.boss.enemy.y == 3000 and len(self.enemies) == 0:
          self.message.PositionSetzen(300, 300)
          self.message.TextSetzen("It is not over!!")
      else:
          self.message.PositionSetzen(0, 5000)

      # Bullet Movement
      for bullet in self.bullets[:]:
         if bullet.bullet.y <= -10:
               bullet.bullet.SichtbarkeitSetzen(False)
               self.bullets.remove(bullet)
         else:
               bullet.MoveBullet()

      # Enemy Bullet Movement
      for bullet1 in self.enemyBullets[:]:
         self.v.playerIsHit(bullet1.ebullet.x, bullet1.ebullet.y)
         bullet1.MoveEnemyBullet()
         if bullet1.ebullet.y >= 800:
               self.enemyBullets.remove(bullet1)

      # Boss Bullet Movement
      for bullet2 in self.bossBullets[:]:
         self.v.playerIsHit(bullet2.bbullet.x, bullet2.bbullet.y)
         bullet2.MoveBossBullet()
         if bullet2.bbullet.y >= 800:
               self.bossBullets.remove(bullet2)
# Win Condition
      if self.v.score >= 15:
          self.v.bg.GroesseSetzen(3000, 3000)
          self.v.bg.FarbeSetzen("weiss")
          self.v.bg.GanzNachVornBringen()
          self.v.gameoverstate.TextSetzen("You win!!")
          self.v.gameoverstate.FarbeSetzen("grün")
          self.v.gameoverstate.TextGroesseSetzen(80)
          self.v.gameoverstate.PositionSetzen(300, 300)
          self.v.gameoverstate.GanzNachVornBringen()
          super().Anhalten()

# Player Death
      if self.v.lives <= 0:
         super().Anhalten()

    def createEnemy(self):
      # spread enemies out horizontally so they don't spawn stacked
      x = 100 + (self.fixedEnemyCount - 1) * 150
      self.enemies.append(self.m.ENEMY( x, 50))
      print("New Enemy")
   # Shooting Movement
    def EnemyShooting(self, enemy1):
      if enemy1.lastBullet is None or enemy1.lastBullet.ebullet.y >= 500:
         newBullet = enemy1.createEBullet()
         enemy1.lastBullet = newBullet
         self.enemyBullets.append(newBullet)

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
