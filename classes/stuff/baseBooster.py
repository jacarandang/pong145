import time

from baseStuff import baseStuff

class baseBooster(baseStuff):

    def __init__(self, dx, dy, x, y):
        self.dx = dx
        self.dy = dy
        baseStuff.__init__(self, x, y, 150, 50)
        self.timer = time.time()

    def update(self):
        dt = time.time() - self.timer
        dt *= 100
        baseStuff.checkInRange(self)
        for ball in self.balls:
            if self.inRange[ball]:
                ball.dx += self.dx*dt
                ball.dy += self.dy*dt
        self.timer = time.time()
