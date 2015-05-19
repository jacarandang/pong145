import pygame
from pygame.locals import *

import os, sys

def loadImage(image, colorkey = -1):
    img = os.path.join("resource", image)
    image = pygame.image.load(img).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

class Button(pygame.sprite.Sprite):

	def __init__(self, image, (x, y), action, selected = False):
		pygame.sprite.Sprite.__init__(self)
		if(selected):
			image = pygame.transform.scale(image, (image.get_width()+20, image.get_height()+20))
		self.bimage = image
		self.image = image.copy()
		self.rect = self.image.get_rect()
		self.action = action

		self.enlarged = False

		self.x = x
		self.y = y
		self.rect.center = self.x, self.y

	def update(self):
		if(self.rect.collidepoint(pygame.mouse.get_pos())):
			if not self.enlarged:
				self.enlarged = True
				self.rect.inflate_ip(20, 20)
				self.image = pygame.transform.scale(self.bimage, (self.rect.size))
		else:
			if self.enlarged:
				self.enlarged = False
				self.rect.inflate_ip(-20, -20)
				self.image = pygame.transform.scale(self.bimage, (self.rect.size))

	def click(self):
		if(self.rect.collidepoint(pygame.mouse.get_pos())):
			self.action()
			return True
		return False
