import time

class basePong:

    def __init__(self, (x, y)):
        self.x = x
        self.y = y
        self.h = 150
        self.w = 10

        self.sy = 200.00
        self.dy = 0
        self.time = time.time()

        self.points = 0

    def update(self):
        dt = time.time() - self.time
        dt *= 100
        if not (self.y + self.dy*dt - self.h/2 < 0 or self.y + self.dy*dt + self.h/2 > 600):
            self.y += self.dy*dt
        else:
            self.dy = 0
        self.time = time.time()

    def startMovingUp(self):
        self.dy = -5
        self.time = time.time()

    def startMovingDown(self):
        self.dy = 5
        self.time = time.time()

    def stopMoving(self):
        self.dy = 0
