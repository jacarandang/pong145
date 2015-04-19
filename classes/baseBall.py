
import random, time

class baseBall:

    def __init__(self, x = 400, y = 300):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.r = 5
        self.dt = time.time()

    def initiate(self):
        self.dx = random.choice([-5, 5])
        self.dy = random.randint(-3, 3)

    def update(self):
        delta = time.time() - self.dt
        self.x += self.dx*delta
        self.y += self.dy*delta
        self.dt = time.time()
