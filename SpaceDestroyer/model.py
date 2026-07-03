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

    class ENEMY():
        def __init__(self):
            self.enemy = FIGUR()
            self.enemy.FigurteilFestlegenEllipse(500, 50, 80, 80, "grün")

        def MoveEnemy(self):
            self.enemy.PositionSetzen(self.enemy.x + 1, self.enemy.y + random.randint(-1, 1))
            if self.enemy.x >= 800:
                self.enemy.PositionSetzen(-200, 50)
