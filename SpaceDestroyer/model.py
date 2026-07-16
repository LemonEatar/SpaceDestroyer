from graphics_and_games_klassen import *

class MODEL(EREIGNISBEHANDLUNG):

    def __init__(self):
        super().__init__()
    class BULLET():
        def __init__(self, x, y):
            self.bullet = DREIECK()
            self.bullet.PositionSetzen(x, y)
            self.bullet.GroesseSetzen(5,15)
            self.bullet.FarbeSetzen("schwarz")

        def MoveBullet(self):
             self.bullet.PositionSetzen(self.bullet.x, self.bullet.y-1)
        def __del__(self) :
            # deconstruct
            print("Bullet destroyed")

    

    class BOSS():
        def __init__(self):
            self.enemy = FIGUR()
            self.isAlive = True
            self.bossLives = 50
            self.enemy.FigurteilFestlegenEllipse(-10, 50, 50, 50, "blau")
        def PositionSetzen(self, x, y):
            self.enemy.PositionSetzen(x, y)
        def MoveBoss(self):
            self.enemy.PositionSetzen(self.enemy.x + 0.75, self.enemy.y + random.randint(-1, 1))
            if self.enemy.x >= 1200:
                self.enemy.PositionSetzen(-200, 50)
        def isHit(self):
            if self.enemy.BeruehrtFarbe("schwarz"):
                self.bossLives -= 1
                if self.bossLives <= 0:
                    self.isAlive = False
                    return True
        def createBossBullet(self):
            return self.BBULLET(self.enemy.x +15, self.enemy.y+10)
        class BBULLET():
            def __init__(self, x, y):
                self.bbullet = DREIECK()
                self.bbullet.PositionSetzen(x,y)
                self.bbullet.GroesseSetzen(5,15)
                self.bbullet.FarbeSetzen("grau")
                self.bbullet.Drehen(180)
            
            def MoveBossBullet(self):
                self.bbullet.PositionSetzen(self.bbullet.x, self.bbullet.y+2)
            def __del__(self) :
                # deconstruct
                print("Bullet destroyed")

    class ENEMY():
        def __init__(self, x=500, y=50):
            self.enemy = FIGUR()
            self.enemy.FigurteilFestlegenEllipse(0, 0, 80, 80, "grün")
            self.enemy.PositionSetzen(x, y)
            self.zustand = 1
            self.lastBullet = None
        def PositionSetzen(self, x, y):
            self.enemy.PositionSetzen(x, y)
        def MoveEnemy(self):
            self.enemy.PositionSetzen(self.enemy.x + 0.5, self.enemy.y + random.randint(-1, 1))
            if self.enemy.x >= 1200:
                self.enemy.PositionSetzen(-200, 50)
        def isHit(self):
            if self.enemy.BeruehrtFarbe("schwarz"):
                self.enemy.PositionSetzen(-30,3000)
                print("Hit")
                return True
        def createEBullet(self):
            return self.EBULLET(self.enemy.x+30, self.enemy.y+10)
        class EBULLET():
            def __init__(self, x, y):
                self.ebullet = DREIECK()
                self.ebullet.PositionSetzen(x,y)
                self.ebullet.GroesseSetzen(5,15)
                self.ebullet.FarbeSetzen("lila")
                self.ebullet.Drehen(180)
            
            def MoveEnemyBullet(self):
                self.ebullet.PositionSetzen(self.ebullet.x, self.ebullet.y+1)
            def __del__(self) :
                # deconstruct
                print("Bullet destroyed")
