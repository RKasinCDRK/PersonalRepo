import pygame
import os
from Constants import *
from Images import background, clouds, pipes, castle

class Basic_config:
    def __init__(self):
        self._background = background()
        self._clouds = clouds()
        self._castle = castle()

    def show(self, img, screen, array=None, coords=None):
        if array is not None:
            for i in array:
                screen.blit(img, i)
        else:
            screen.blit(img, coords)