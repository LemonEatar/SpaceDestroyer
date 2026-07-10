from graphics_and_games_klassen import *

class MODEL(EREIGNISBEHANDLUNG):

    def __init__(self):
        super().__init__()
        self.score = 0

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

    

    class BOSSBULLET():
        def __init__(self, x, y):
            self.bossbullet = DREIECK()
            self.bossbullet.PositionSetzen(x,y)
            self.bossbullet.GroesseSetzen(5,15)
            self.bossbullet.FarbeSetzen("blau")
            self.bossbullet.Drehen(180)
        
        def MoveBossBullet(self):
            self.bossbullet.PositionSetzen(self.bossbullet.x, self.bossbullet.y+1.5)
        def __del__(self) :
            # deconstruct
            print("Bullet destroyed")

    class ENEMY():
        def __init__(self):
            self.enemy = FIGUR()
            self.enemy.FigurteilFestlegenEllipse(500, 50, 80, 80, "grün")
            self.zustand = 1
        def FarbeSetzen(self, farbe):
            self.FarbeSetzen(farbe)
        def PositionSetzen(self, x, y):
            self.PositionSetzen(x, y)
        def MoveEnemy(self):
            self.enemy.PositionSetzen(self.enemy.x + 0.5, self.enemy.y + random.randint(-1, 1))
            if self.enemy.x >= 800:
                self.enemy.PositionSetzen(-200, 50)
        def isHit(self):
            if self.enemy.BeruehrtFarbe("schwarz"):
                print("Hit")
                self.enemy.PositionSetzen(-300, -100)
            if self.enemy.x == -300:
                print("Enemy destroyed")
                self.zustand = 0
        def createEBullet(self):
            return self.EBULLET(self.enemy.x +230, self.enemy.y+10)
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
