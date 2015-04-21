import os, sys, time

import pygame
from pygame.locals import *

from classes.board import boardSprite
from classes.pong import pongSprite
from classes.ball import ballSprite
from classes.stuff import splitterSprite

class Main:

    def __init__(self, screen):
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
        self.stuffGroup.add(self.splitter)

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
                    self.player1.startMovingUp()
                elif event.key == K_DOWN:
                    self.player1.startMovingDown()
                if event.key == K_a:
                    self.player2.startMovingUp()
                elif event.key == K_z:
                    self.player2.startMovingDown()
            elif event.type == KEYUP:
                if event.key in [K_UP, K_DOWN]:
                    self.player1.stopMoving()
                if event.key in [K_a, K_z]:
                    self.player2.stopMoving()

    def start(self):
        self.running = True
        self.ball.initiate()
        while(self.running):
            self.check_events()
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

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Pong")
    pygame.key.set_repeat(1, 10)
    screen = pygame.display.set_mode((800, 600))
    game = Main(screen)
    game.start()
