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
