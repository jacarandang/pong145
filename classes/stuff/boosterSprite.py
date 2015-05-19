import pygame
from pygame.locals import *

from baseBooster import baseBooster

class boosterSprite(pygame.sprite.Sprite, baseBooster):

    def __init__(self,  dx, dy, x, y, image = None, onMouse = False):
        pygame.sprite.Sprite.__init__(self)
        baseBooster.__init__(self, dx, dy, x, y)
        self.rect = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w, self.h)
        if not image:
            self.image = pygame.Surface((self.rect.w, self.rect.h)).convert()
            self.image.fill((255, 255, 200))
        else:
            self.image = image
        self.onMouse = onMouse
        self.update()

    def update(self):
        baseBooster.update(self)
        if self.onMouse:
            self.rect.center = pygame.mouse.get_pos()
        else:
            self.rect.center = self.x, self.y
