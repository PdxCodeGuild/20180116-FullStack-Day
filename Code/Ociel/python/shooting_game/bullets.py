import pygame as pg
from settings import *


# bullet_img = pg.image.load('img/fire_ball.png')

class Bullets(pg.sprite.Sprite):
    def __init__(self, pos, angle):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('img/fire_ball.png')
        self.image = pg.transform.scale(self.image, (40 ,40))
        self.rect = self.image.get_rect()
        self.pos = pg.math.Vector2(pos)
        self.rect.bottom = self.pos.x       # This assigns the bottom of the image to have the X Position
        self.rect.top = self.pos.y          # This assigns the top of the image to have the Y Position
        self.rect.center = self.pos         # Puts both the X and the Y into the center position for the image
        self.speedy = -10                   # -10 will make the bullet go up since it is only working on the Y Axis.
                                            #               Y starts at the Bottom of the screen with 800. A negative
                                            #               number will make it the bullet or 'image' go up.



    def update(self):
        # This only makes the bullet go up.
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()



