import time

from baseStuff import baseStuff

class baseBooster(baseStuff):

    def __init__(self, dx, dy, x, y):
        self.dx = dx
        self.dy = dy
        baseStuff.__init__(self, x, y, 100, 50)
        self.timer = time.time()
        self.timeout = time.time()
        self.type = "booster"

    def update(self, fxn = None):
        dt = time.time() - self.timer
        dt *= 100
        baseStuff.checkInRange(self)
        if time.time() - self.timeout >= 3:
            for ball in self.balls:
                if self.inRange[ball]:
                    ball.dx += self.dx
                    ball.dy += self.dy
                    self.timeout = time.time()
                    if fxn is not None:
                        fxn()
        self.timer = time.time()
