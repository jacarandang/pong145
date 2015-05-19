import pygame
from pygame.locals import *

from baseSplitter import baseSplitter

class splitterSprite(pygame.sprite.Sprite, baseSplitter):

    def __init__(self, x, y, main, image = None, onMouse = False):
        pygame.sprite.Sprite.__init__(self)
        baseSplitter.__init__(self, x, y, main)
        self.rect = pygame.Rect(self.x - self.w/2, self.y - self.h/2, self.w, self.h)
        if not image:
            self.image = pygame.Surface((self.rect.w, self.rect.h)).convert()
            self.image.fill((255, 255, 200))
        else:
            self.image = image
        self.onMouse = onMouse
        self.update()

    def update(self):
        if self.onMouse:
            self.x, self.y = pygame.mouse.get_pos()
        baseSplitter.update(self)
        self.rect.center = self.x, self.y
