import pygame
from pygame.locals import *

from baseBoard import baseBoard

class boardSprite(baseBoard, pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        baseBoard.__init__(self)

        self.image = pygame.Surface((self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.center = 0, 0

    def update(self):
        pass
