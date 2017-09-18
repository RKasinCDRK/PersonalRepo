import pygame
from Constants import *
from Images import clouds, pipes, bricks, coin, peach

def Sprite_init():
    p = 0
    wc = 0
    b = 0
    c = 0
    ALL_SPRITES = pygame.sprite.Group(p, wc, b, c, Peach())


class Pipes(pygame.sprite.Sprite):
    def __init__(self, size, position):
        super().__init__()
        self.pipes = pipes()
        self.image = self.pipes[size]
        self.rect = self.image.get_rect()
        self.rect.x = position(0)
        self.rect.y = position(1)

class WalkableClouds(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.clouds = clouds()
        self.image = self.clouds['img']
        self.rect = self.image.get_rect()
        self.rect.x = position(0)
        self.rect.y = position(1)


class Bricks(pygame.sprite.Sprite):
    def __init__(self, counter, position):
        super().__init__()
        self.bricks = bricks()
        self.image = self.bricks[counter]
        self.rect = self.image.get_rect()
        self.rect.x = position(0)
        self.rect.y = position(1)

class Coin(pygame.sprite.Sprite):
    def __init__(self, counter, position):
        super().__init__()
        self.coin = coin()
        self.image = self.coin[0]
        self.rect = self.image.get_rect()
        self.rect.x = position(0)
        self.rect.y = position(1)

class Peach(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.peach = peach()
        self.image = self.peach[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = PEACH_POS
