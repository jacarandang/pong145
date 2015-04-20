from baseStuff import baseStuff

class baseBooster(baseStuff):

    def __init__(self, dx, dy, x, y):
        self.dx = dx
        self.dy = dy
        baseStuff.__init__(self, x, y, 150, 50)
        self.ball = None

    def setBall(self, ball):
        self.ball = ball

    def update(self):
        if self.ballInRange():
            self.ball.dx += self.dx
            self.ball.dx += self.dy
