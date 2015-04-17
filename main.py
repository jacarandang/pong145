import os, sys, time

import pygame
from pygame.locals import *

from classes import boardSprite
from classes import pongSprite

class Main:

    def __init__(self, screen):
        self.screen = screen
        self.bg = pygame.Surface(screen.get_size()).convert()
        self.bg.fill((0, 0, 0))

        self.clock = pygame.time.Clock();
        self.running = False

        self.board = boardSprite.boardSprite()

        self.player1 = pongSprite.pongSprite()

        self.spriteGroup = pygame.sprite.Group()
        self.spriteGroup.add(self.board, self.player1)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

    def start(self):
        self.running = True
        while(self.running):
            self.check_events()
            self.clock.tick(120)

            self.screen.blit(self.bg, (0, 0))

            self.spriteGroup.update()
            self.spriteGroup.draw(self.screen)

            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Pong")

    screen = pygame.display.set_mode((800, 600))
    game = Main(screen)
    game.start()
