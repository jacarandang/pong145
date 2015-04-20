import pygame
from pygame.locals import *

from baseBoard import baseBoard
from classes import utilities

class boardSprite(baseBoard, pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        baseBoard.__init__(self)

        self.image = utilities.loadImage("stage.jpg", -1)
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0

    def update(self):
        pass
