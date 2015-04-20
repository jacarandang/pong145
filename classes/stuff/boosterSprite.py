import pygame
from pygame.locals import *

from baseBooster import baseBooster
class boosterSprite(pygame.sprite.Sprite, baseBooster):

    def __init__(self, dx, dy, x, y):
        pygame.sprite.Sprite.__init__(self)
        baseBooster.__init__(self, dx, dy, x, y)
        self.rect = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w, self.h)
        self.image = pygame.Surface((self.rect.w, self.rect.h)).convert()
        self.image.fill((255, 255, 255))

    def update(self):
        baseBooster.update(self)
        self.rect.center = self.x, self.y
