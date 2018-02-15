import pygame as pg
from settings import *
import random
vec = pg.math.Vector2


class Mob(pg.sprite.Sprite):
    def __init__(self, initial_x, initial_y):
        self.initial_x = initial_x   # Initial position (X,Y)
        self.initial_y = initial_y
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Enemies/enemyBlack1.png').convert()
        self.image = pg.transform.scale(self.image, (60,60))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # self.pos = vec(self.initial_x,self.initial_y)
        # self.vel = vec(0,0)
        # self.acc = vec(0,0)
        self.rect.x = random.randrange(0, WIDTH)          # Velocity         (X,Y)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(-2, 2)  #Speed going down             # Acceleration     (X,Y)
        self.speedx = random.randrange(-1,1)  #Speed going side to side

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25\
                or self.rect.right > WIDTH + 25:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = WIDTH
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        if self.rect.y < 0:
            self.rect.y = HEIGHT


