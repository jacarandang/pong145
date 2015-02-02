import os, sys, time

import pygame
from pygame.locals import *

class Main:

    def __init__(self, screen):
        self.screen = screen
        self.bg = pygame.Surface(screen.get_size()).convert()
        self.bg.fill((0, 0, 0))

        self.clock = pygame.time.Clock();
        self.running = False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

    def start(self):
        self.running = True
        while(self.running):
            self.check_events()

            self.screen.blit(self.bg, (0, 0))

            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    game = Main(screen)
    game.start()
