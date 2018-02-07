# Sprite calsses for platform game
import pygame as pg
from settings import *
from bullets import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('img/soldier_1.png')
        self.image = pg.transform.scale(self.image,(60,60))
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.rect.center = self.pos                     # Initial position (X,Y)
        self.vel = vec(0,0)                             # Velocity         (X,Y)
        self.acc = vec(0,0)                             # Acceleration     (X,Y)
        self.rot = 0
        self.angle = 0


    def get_keys(self):
        # The Key pressed is going to control the
        # acceleration. Which means that the acceleration
        # should be Zero unless you are pressing the key.
        self.acc = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC # Accelerate to Left
            # self.player_rotate_left()
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC  # Accelerate to Right
            # self.player_rotate_right()
        if keys[pg.K_UP]:
            self.acc.y = -PLAYER_ACC # Accelerate to Left
        if keys[pg.K_DOWN]:
            self.acc.y = PLAYER_ACC  # Accelerate to Right

    def wrap_around(self):
        # The Player Wraps around the screen if it goes out of bounds
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT

    def udpate_image_position_vel_acc(self):
        # We add friction just so the player doesnt go
        # as fast as it is going.
        self.acc += self.vel * PLAYER_FRICTION
        self.vel += self.acc                       # The acceleration adds to the Velocity
        self.pos += self.vel + 0.5 * self.acc      # Equations of Motion
        self.rect.center = self.pos                # Gives the new 'image' the added new position after
                                                            # handling (x,y) inside acc, vel, and pos.

    def update(self):

        self.get_keys()
        self.udpate_image_position_vel_acc()
        self.wrap_around()



    def shoot(self,all_sprite, bullet_group):
        self.bullet = Bullets(self.rect.center, self.angle)
        all_sprite.add(self.bullet)
        bullet_group.add(self.bullet)





    #   This code rotates the player image but the surface area does not rotate.
    #   i am still trying to figure out how to update. the surface image and the pass the new
    #   position to bullet so that it can also update and turn with the player.
    # def player_rotate_right(self):
    #     self.angle += 5
    #     self.image = pg.transform.rotozoom(self.orig_image, -self.angle,1)
    #     self.rect = self.image.get_rect(center=self.rect.center)
    #     self.bullet.set_rect(self.rect)
    #
    # def player_rotate_left(self):
    #     self.angle += 5
    #     self.image = pg.transform.rotozoom(self.orig_image, self.angle,1)
    #     self.rect = self.image.get_rect(center=self.rect.center)
    #     self.bullet.set_rect(self.rect)