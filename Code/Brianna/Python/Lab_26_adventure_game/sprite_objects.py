"""
Module for managing sprites, walls, objects. EDIT TO REFLECT OBJECTS AND THEIR CLASSES PLUS WALLS, ETC
"""
import pygame

from spritesheet_functions import SpriteSheet

# These constants define our sprite types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite


#### List tile lists????   THIS WILL CHANGE >>>  No longer using a cut up sprite sheet

TREE = pygame.image.load("images/grass_etc_tile_set/png/1x/non_tile/Tree.png")
GRASS_RIGHT = pygame.image.load()
GRASS_MIDDLE = pygame.image.load()
STONE_PLATFORM_LEFT =  pygame.image.load()
STONE_PLATFORM_MIDDLE = pygame.image.load()   ###  >>> Not using platforms anymore/not side-scrolling. Use walls for some similar effects.
STONE_PLATFORM_RIGHT = pygame.image.load()


class Wall(pygame.sprite.Sprite):   ### Make walls here? Probably don't need to use spritesheet_functions now...
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        sprite_sheet = SpriteSheet("tiles_spritesheet.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],  ### this is probably referenced elsewhere and needs to be changed
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()


class MovingPlatform(Platform):   #Also referenced elsewhere and needs to be changed
    """ This is a fancier platform that can actually mainLoop. """

    def __init__(self, sprite_sheet_data):

        super().__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):
        """ Move the moving sprites.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving objects have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1


class Willowisp():
    """ This sets up the methods and 'Character' that tasks are given to the player through. """
    def __init__(self):
        self.name = "Willow"
        self.location = # Random location within the area just outside of main characters home.
        self.converse = converse  # figure out how to do this.


class Enemies():
    """ This class sets up the enemies for the main character to encounter """

    def __init__(self):
        self.max_hit_points = 20
        self.current_hit_points = 20
        self.max_speed = 10
        self.armour_amount = 8

    def attack(self):
        # an if statement
        pass
