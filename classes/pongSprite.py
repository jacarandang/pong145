import pygame
from pygame.locals import *

from basePong import basePong

class pongSprite(basePong, pygame.sprite.Sprite):

    def __init__(self, (x, y)):
        pygame.sprite.Sprite.__init__(self)
        basePong.__init__(self, (x, y))
        self.rect = pygame.Rect(self.x-self.w/2.00, self.y-self.h/2.00, self.w, self.h)
        self.image = pygame.Surface((self.rect.w, self.rect.h))
        self.image.fill((255, 255, 255))

    def update(self):
        basePong.update(self)
        self.rect.center = self.x, self.y
