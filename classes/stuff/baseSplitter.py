import time

from baseStuff import baseStuff
from classes.ball import ballSprite

class baseSplitter(baseStuff):

    def __init__(self, x, y, main):
        baseStuff.__init__(self, x, y, 50, 50)
        self.timer = time.time()
        self.main = main

    def update(self):
        baseStuff.checkInRange(self)
        for ball in self.balls:
            if self.inRange[ball]:
                self.main.addBall(ball.x, ball.y, ball.dx, -ball.dy)
