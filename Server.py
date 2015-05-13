from classes.ball import baseBall
from classes.pong import basePong
from classes.connections import *

class ServerGame:

    def __init__(self):
        self.ball = baseBall.baseBall()

        self.playerl = basePong((10, 300))
        self.playerr = basePong((790, 300))

        self.ball.setLeftPong(self.playerl)
        self.ball.setRightPong(self.playerr)

    def start()
        self.ball.initiate()
        running = True
        while(running):
            self.ball.update()
            self.playerl.update()
            self.playerr.update()

            if self.ball.outOfBounds():
                running = False
