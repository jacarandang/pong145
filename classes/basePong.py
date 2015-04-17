class basePong:

    def __init__(self, (x, y)):
        self.x = x
        self.y = y
        self.h = 50
        self.w = 5

        self.sy = 5

    def update(self):
        pass

    def moveUp(self, dt):
        self.y -= self.sy*dt

    def moveDown(self, dt):
        self.y += self.sy*dt
