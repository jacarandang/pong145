import time

from classes.ball import baseBall
from classes.pong import basePong
from classes.connections import Server
from classes.stuff import baseBooster
from classes.stuff import baseSplitter

import pygame

class ServerGame:

    def __init__(self, server):
        self.ball = baseBall.baseBall()

        self.playerl = basePong.basePong((10, 300))
        self.playerr = basePong.basePong((790, 300))

        self.ball.setLeftPong(self.playerl)
        self.ball.setRightPong(self.playerr)


        self.balls = [self.ball]
        self.timer = time.time()

        self.server = server
        self.server.send_to_all("COUNTDOWN")

        self.stuffGroup = []
        count = 0
        while(True):
            msg = self.server.wait_message()
            if msg[1] == "READY":
                count+=1
            if count == 2:
                break

        self.start()

    def add_ball(self, x, y, dx, dy):
        ball = baseBall.baseBall(x, y, dx, dy)
        ball.setLeftPong(self.playerl)
        ball.setRightPong(self.playerr)
        for stuff in self.stuffGroup:
            stuff.addBall(ball)
        self.balls.append(ball)

    def remove_ball(self, ball):
        for stuff in self.stuffGroup:
            stuff.removeBall(ball)
        self.balls.remove(ball)

    def process_message(self):
        for msg in self.server.get_all():
            print msg
            if msg[1] == "up":
                if msg[0] == self.server.player1:
                    self.server.send_to_all("player 1 up")
                    self.playerl.startMovingUp()
                else:
                    self.server.send_to_all("player 2 up")
                    self.playerr.startMovingUp()

            elif msg[1] == "down":
                if msg[0] == self.server.player1:
                    self.server.send_to_all("player 1 down")
                    self.playerl.startMovingDown()
                else:
                    self.server.send_to_all("player 2 down")
                    self.playerr.startMovingDown()


            elif msg[1] == "stop":
                if msg[0] == self.server.player1:
                    self.server.send_to_all("player 1 stop")
                    self.playerl.stopMoving()
                else:
                    self.server.send_to_all("player 2 stop")
                    self.playerr.stopMoving()

    def update_status(self):
        for i in range(len(self.balls)):
            ball = self.balls[i]
            self.server.send_to_all("ball "+str(i)+" "+str(ball.x)+" "+str(ball.y)+" "+str(ball.dx)+" "+str(ball.dy)+"\n")
        self.server.send_to_all("player 1 pos " + str(self.playerl.x) + " " + str(self.playerl.y)+"\n")
        self.server.send_to_all("player 2 pos " + str(self.playerr.x) + " " + str(self.playerr.y)+"\n")

    def start(self):
        (x, y) = self.ball.initiate()
        running = True

        self.server.send_to_all(str(x)+" "+str(y))
        self.playerl.time = time.time()
        self.playerr.time = time.time()

        booster = baseSplitter.baseSplitter(400, 300, self)
        booster.addBall(self.ball)
        splitter = baseSplitter.baseSplitter(400, 400, self)
        splitter.addBall(self.ball)

        self.stuffGroup = [booster, splitter]

        while(running):
            for ball in self.balls:
                if ball.out:
                    self.remove_ball(ball)

            if len(self.balls) == 0:
                self.server.send_to_all("GAMEOVER\n")
                self.side = self.ball.side
                self.server.send_to_all("WIN "+str(self.ball)+"\n")
                break

            self.process_message()
            for ball in self.balls:
                ball.update()
            self.playerl.update()
            self.playerr.update()
            for s in self.stuffGroup:
                s.update()

            if time.time() - self.timer >= .25:
                self.timer = time.time()
                self.update_status()

if __name__ == '__main__':
    print "Enter address"
    add = raw_input()
    print "Enter port"
    port = raw_input()

    server = Server.Server(add, port)

    print "Server started, Waiting for players"
    server.start()
    server.begin_listening()
    print "Players connected, starting game"
    game = ServerGame(server)
    server.kill_all()
