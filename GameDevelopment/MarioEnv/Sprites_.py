import pygame
from itertools import cycle
from Constants import *
from Images import *

class _Sprites:
    def __init__(self):
        self.Sprite_init()

    def Sprite_init(self):
        #TO DO: Add all the missing sprite groups that were defined as class but not inserted below
        bricks_counter = cycle(range(5))
        pipes = pygame.sprite.Group(Pipes(size=values[0], position=(values[1], values[2])) for values in PIPES_POSITION)
        wc = pygame.sprite.Group(WalkableClouds(position=pos) for pos in CLOUD_POSITIONS)
        bricks = pygame.sprite.Group(Bricks(counter=bricks_counter.__next__(), position=pos) for pos in BRICK_POSITIONS)
        ground = pygame.sprite.Group(Ground(position=pos) for pos in GROUND_POSITIONS)
        coins = pygame.sprite.Group(Coin(position=pos) for pos in COIN_POSITIONS)
        stairs = pygame.sprite.Group(Stairs(position=pos) for pos in STAIRS_POSITION)
        self.ENTITIES = pygame.sprite.Group(pipes, wc, bricks, coins, stairs, ground)

    def update(self):
        self.ENTITIES.update()

class Pipes(pygame.sprite.Sprite):
    def __init__(self, size, position):
        super().__init__()
        self.pipes = pipes()
        self.image = self.pipes[size]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position


class WalkableClouds(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.clouds = clouds()
        self.image = self.clouds['img']
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position


class Ground(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.ground = ground()
        self.image = self.ground
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position


class Bricks(pygame.sprite.Sprite):
    def __init__(self, counter, position):
        super().__init__()
        self.bricks = bricks()
        self.image = self.bricks[counter]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position


class Mystery_Blocks(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.counter = cycle(range(2))
        self.blocks = mystery_blocks()
        self.image = self.blocks[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self):
        self.image = self.blocks[self.counter.__next__()]


class Stairs(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = stairs()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position


class Coin(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.coin_counter = cycle(range(4))
        self.coin = coin()
        self.image = self.coin[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self):
        self.image = self.coin[self.coin_counter.__next__()] #TO DO: Fix coin counter to only be called once

class Peach(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.peach = peach()
        self.image = self.peach[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = PEACH_POS

    def update(self):
        pass
        #TO DO: Make an update function for peach's movements

'''
SEPARATION: BELOW SPRITES NEED TO BE ADDED TO THE SPRITES ARRAY AND MODIFIED.
'''

class Goombas(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.counter = cycle(range(2))
        self.goombas = goombas()
        self.image = self.goombas[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self, x): #TO DO: Figure out collision detection with goombas
        self.rect.x += GOOMBA_SPEED
        self.image = self.goombas[self.counter.__next__()]


class Skeletons(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.counter = cycle(range(2))
        self.skeletons = skeletons()
        self.image = self.skeletons[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self, x):  # TO DO: Figure out collision detection with goombas
        self.rect.x += SKELLY_SPEED
        self.image = self.skeletons[self.counter.__next__()]