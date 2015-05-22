import time
from math import degrees, radians, atan2, cos, sin

from baseStuff import baseStuff
from classes.ball import ballSprite

class baseSplitter(baseStuff):

    def __init__(self, x, y, main):
        baseStuff.__init__(self, x, y, 30, 30)
        self.timer = time.time()
        self.main = main
        self.timeout = time.time()
        self.type = "splitter"
        self.cost = 30

    def update(self):
        baseStuff.checkInRange(self)
        if time.time() - self.timeout >= 3:
            for ball in self.balls:
                if self.inRange[ball]:
                    ball_speed = (ball.dx**2+ball.dy**2)**0.5
                    ball_angle = degrees(atan2(ball.dy, ball.dx))
                    ball_angle1 = ball_angle + 3
                    ball_angle2 = ball_angle - 3
                    ball.dx = ball_speed*cos(radians(ball_angle1))
                    ball.dy = ball_speed*sin(radians(ball_angle1))
                    ndx = ball_speed*cos(radians(ball_angle2))
                    ndy = ball_speed*sin(radians(ball_angle2))
                    self.main.add_ball(ball.x, ball.y, ndx, ndy)
                    self.timeout = time.time()
