import time

class baseStuff:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.balls = []
        self.inRange = {}

    def addBall(self, ball):
        self.balls.append(ball)
        self.inRange[ball] = False

    def removeBall(self, ball):
        self.balls.remove(ball)
        self.time.pop(ball)
        self.inRange(ball)

    def checkInRange(self):
        for ball in self.balls:
            if ball.x - ball.r < self.x + self.w/2 and ball.x + ball.r > self.x - self.w/2 and ball.y - ball.r < self.y + self.h/2 and ball.y + ball.r > self.y - self.w/2:
                self.inRange[ball] = True
            else:
                self.inRange[ball] = False
