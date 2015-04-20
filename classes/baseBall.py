
import random, time

class baseBall:

    def __init__(self, x = 400, y = 300):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.r = 8
        self.dt = time.time()
        self.leftPong = None
        self.rightPong = None
        self.out = False

    def setLeftPong(self, leftPong):
        self.leftPong = leftPong

    def setRightPong(self, rightPong):
        self.rightPong = rightPong

    def initiate(self):
        self.dx = random.choice([3, 3])
        self.dy = random.choice([3, -3])

    def update(self):
        delta = time.time() - self.dt
        delta *= 100
        self.x += self.dx*delta
        self.y += self.dy*delta
        self.dt = time.time()

        if self.onTopBot():
            self.dy = -self.dy
        # if self.onLeftRight():
        #     self.dx = -self.dx
        self.onPong()

    def onTopBot(self):
        return self.y + self.r >= 600 or self.y - self.r < 0

    def onLeftRight(self):
        return self.x + self.r >= 800 or self.x - self.r < 0

    def onPong(self):
        if self.leftPong is None or self.rightPong is None:
            pass
        else:
            if self.dx < 0:
                if self.y < self.leftPong.y + self.leftPong.h/2 and self.y > self.leftPong.y - self.leftPong.h/2 and self.x < self.leftPong.x + self.leftPong.w/2 and self.x > self.leftPong.x - self.leftPong.w/2:
                    self.dx = -self.dx
            else:
                if self.y < self.rightPong.y + self.rightPong.h/2 and self.y > self.rightPong.y - self.rightPong.h/2 and self.x < self.rightPong.x + self.rightPong.w/2 and self.x > self.rightPong.x - self.rightPong.w/2:
                    self.dx = -self.dx
