import pygame
from pygame.locals import *

from baseBall import baseBall

class ballSprite(baseBall, pygame.sprite.Sprite):

    def __init__(self, x = 400, y = 300, dx = 0, dy = 0):
        pygame.sprite.Sprite.__init__(self)
        baseBall.__init__(self, x, y, dx, dy)
        self.rect = pygame.Rect(self.x + self.r, self.y + self.r, self.r * 2, self.r * 2)
        self.image = pygame.Surface((self.rect.width, self.rect.height)).convert()
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image, (200, 200, 200), (self.rect.width/2, self.rect.height/2), self.r)
        self.image.set_colorkey((0, 0, 0), RLEACCEL)

    def update(self):
        baseBall.update(self)
        self.rect.center = self.x, self.y
