import time

class baseStuff:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ball = None

    def setBall(self, ball):
        self.ball = ball

    def ballInRange(self):
        if self.ball is None:
            return False
        else:
            if self.ball.x - self.ball.r < self.x + self.w/2 and self.ball.x + self.ball.r > self.x - self.w/2 and self.ball.y - self.ball.r < self.y + self.h/2 and self.ball.y + self.ball.r > self.y - self.w/2:
                return True
            return False
