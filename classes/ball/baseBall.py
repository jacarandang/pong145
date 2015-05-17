
import random, time

class baseBall:

    def __init__(self, x = 400, y = 300, dx = 0, dy = 0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = 8
        self.dt = time.time()
        self.leftPong = None
        self.rightPong = None
        self.out = False

    def setLeftPong(self, leftPong):
        self.leftPong = leftPong

    def setRightPong(self, rightPong):
        self.rightPong = rightPong

    def initiate(self, dx = None, dy = None):
        self.dt = time.time()
        if dx is None:
            self.dx = random.choice([3, -3])
        else:
            self.dx = dx

        if dy is None:
            self.dy = random.choice([3, -3])
        else:
            self.dy = dy

        return (self.dx, self.dy)

    def update(self):
        self.onPong()
        self.onTopBot()

        delta = time.time() - self.dt
        delta *= 100
        self.x += self.dx*delta
        self.y += self.dy*delta
        self.dt = time.time()

        self.outOfBounds()

    def onTopBot(self):
        if self.y + self.r >= 600:
            self.y = 600 - self.r - 1
            self.dy = -self.dy
        elif self.y - self.r < 0:
            self.y = self.r
            self.dy = -self.dy

    def outOfBounds(self):
        if self.x < 0 or self.x > 800:
            self.out = True
            return True

    def onPong(self):
        if self.leftPong is None or self.rightPong is None:
            pass
        else:
            #move ball to prevent repeated change
            if self.dx < 0:
                if self.y - self.r < self.leftPong.y + self.leftPong.h/2 and self.y + self.r > self.leftPong.y - self.leftPong.h/2 and self.x - self.r < self.leftPong.x + self.leftPong.w/2 and self.x + self.r > self.leftPong.x - self.leftPong.w/2:
                    self.dx = -self.dx
            else:
                if self.y - self.r < self.rightPong.y + self.rightPong.h/2 and self.y + self.r > self.rightPong.y - self.rightPong.h/2 and self.x - self.r < self.rightPong.x + self.rightPong.w/2 and self.x + self.r > self.rightPong.x - self.rightPong.w/2:
                    self.dx = -self.dx
