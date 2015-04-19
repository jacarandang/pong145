import pygame
from pygame.locals import *

from baseBall import baseBall

class ballSprite(baseBall, pygame.sprite.Sprite):

    def __init__(self, x = 400, y = 300):
        pygame.sprite.Sprite.__init__(self)
        baseBall.__init__(self, x, y)
        self.rect = pygame.Rect(self.x + self.r, self.y + self.r, self.r * 2, self.r * 2)
        self.image = pygame.Surface((self.rect.width, self.rect.height)).convert()
        self.image.fill((0, 0, 0))

        pygame.draw.circle(self.image, (255, 255, 255), (self.rect.width/2, self.rect.height/2), self.r)

    def update(self):
        baseBall.update(self)
        self.rect.center = self.x, self.y
