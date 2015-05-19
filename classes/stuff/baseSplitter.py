import time
from math import degrees, radians, atan2

from baseStuff import baseStuff
from classes.ball import ballSprite

class baseSplitter(baseStuff):

    def __init__(self, x, y, main):
        baseStuff.__init__(self, x, y, 30, 30)
        self.timer = time.time()
        self.main = main
        self.timeout = time.time()

    def update(self):
        baseStuff.checkInRange(self)
        if time.time() - self.timeout >= 3:
            for ball in self.balls:
                if self.inRange[ball]:
                    ball_angle = degrees(atan2(ball.y, ball.x))
                    self.main.addBall(ball.x, ball.y, ball.dx, -ball.dy)
                    self.timeout = time.time()
