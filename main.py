import os, sys, time

import pygame
from pygame.locals import *

from classes.board import boardSprite
from classes.pong import pongSprite
from classes.ball import ballSprite
from classes.stuff import splitterSprite
from classes.connections import Client

pygame.font.init()

class Main:

    def __init__(self, screen, client, player):
        self.screen = screen
        self.bg = pygame.Surface(screen.get_size()).convert()
        self.bg.fill((0, 0, 0))

        self.clock = pygame.time.Clock();
        self.running = False

        self.board = boardSprite.boardSprite()

        self.player1 = pongSprite.pongSprite((10, 300))
        self.player2 = pongSprite.pongSprite((790, 300))

        self.ball = ballSprite.ballSprite(400, 300)
        self.ball.setLeftPong(self.player1)
        self.ball.setRightPong(self.player2)

        self.splitter = splitterSprite.splitterSprite(400, 300, self)
        self.splitter.addBall(self.ball)

        self.spriteGroup = pygame.sprite.Group()
        self.spriteGroup.add(self.player1)
        self.spriteGroup.add(self.player2)
        self.spriteGroup.add(self.ball)

        self.stageGroup = pygame.sprite.Group()
        self.stageGroup.add(self.board)

        self.stuffGroup = pygame.sprite.Group()
        self.stuffGroup.add()

        self.font = pygame.font.Font("resource/font.ttf", 350)

        self.client = client
        self.player = player

    def addBall(self, x, y, dx, dy):
        ball = ballSprite.ballSprite(x, y, dx, dy)
        ball.setLeftPong(self.player1)
        ball.setRightPong(self.player2)
        self.spriteGroup.add(ball)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    if self.player == 1:
                        self.player1.startMovingUp()
                    else:
                        self.player2.startMovingUp()
                    self.client.send("up")
                elif event.key == K_DOWN:
                    if self.player == 1:
                        self.player1.startMovingDown()
                    else:
                        self.player2.startMovingDown()
                    self.client.send("down")
            elif event.type == KEYUP:
                if event.key in [K_UP, K_DOWN]:
                    if self.player == 1:
                        self.player1.stopMoving()
                    else:
                        self.player2.stopMoving()
                    self.client.send("stop")

    def process_message(self):
        for msg in self.client.get_all():
            print msg
            msgs = msg.split()
            if msgs[0] == "player":
                if msgs[1] == "1":
                    if msgs[2] == "up":
                        self.player1.startMovingUp()
                    elif msgs[2] == "down":
                        self.player1.startMovingDown()
                    elif msgs[2] == "stop":
                        self.player1.stopMoving()
                    elif msgs[2] == "pos":
                        x = float(msgs[3])
                        y = float(msgs[4])
                        self.player1.x = x
                        self.player1.y = y
                if msgs[1] == "2":
                    if msgs[2] == "up":
                        self.player2.startMovingUp()
                    elif msgs[2] == "down":
                        self.player2.startMovingDown()
                    elif msgs[2] == "stop":
                        self.player2.stopMoving()
                    elif msgs[2] == "pos":
                        x = float(msgs[3])
                        y = float(msgs[4])
                        self.player2.x = x
                        self.player2.y = y

            if msgs[0] == "ball":
                bx = float(msgs[1])
                by = float(msgs[2])
                self.ball.x = bx
                self.ball.y = by

    def count_down(self):
        rem = 4

        base_time = time.time()
        time_image = self.font.render(str(rem), True, (255, 255, 255), (0, 0, 0))
        time_rect = time_image.get_rect()
        time_rect.center = 400, 300

        self.running = True
        self.quit = False

        overlay = pygame.Surface((800, 600)).convert()
        overlay.fill((0, 0, 0))
        overlay.set_alpha(200)

        while(self.running):
            nrem = int(4 - (time.time() - base_time))
            if(nrem < rem):
                rem = nrem
                time_image = self.font.render(str(rem), True, (255, 255, 255), (0, 0, 0))
                time_rect = time_image.get_rect()
                time_rect.center = 400, 300

            self.clock.tick(60)

            self.screen.blit(self.bg, (0, 0))

            self.stageGroup.update()
            self.stuffGroup.update()
            self.spriteGroup.update()

            self.stageGroup.draw(self.screen)
            self.stuffGroup.draw(self.screen)
            self.spriteGroup.draw(self.screen)

            self.screen.blit(overlay, (0, 0))
            self.screen.blit(time_image, time_rect)


            pygame.display.flip()
            if(rem == 0):
                break

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    self.quit = True

        if self.quit:
            return
        self.client.send("READY")
        self.start()

    def start(self):
        self.running = True
        init = self.client.wait_message().split()
        self.ball.initiate(int(init[0]), int(init[1]))

        while(self.running):
            self.check_events()
            self.process_message()
            self.clock.tick(60)

            self.screen.blit(self.bg, (0, 0))

            self.stageGroup.update()
            self.stuffGroup.update()
            self.spriteGroup.update()

            self.stageGroup.draw(self.screen)
            self.stuffGroup.draw(self.screen)
            self.spriteGroup.draw(self.screen)

            if self.ball.outOfBounds():
                break

            pygame.display.flip()

    def gameover(self):
        pass

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Pong")
    pygame.key.set_repeat(1, 10)
    screen = pygame.display.set_mode((800, 600))

    client = Client.Client()
    client.begin_listening()

    pl = int(client.wait_message())
    game = Main(screen, client, pl)

    while(True):
        if len(client.messageList) != 0:
            msg = client.messageList.pop(0)
            if msg == "COUNTDOWN":
                print msg
                game.count_down()
