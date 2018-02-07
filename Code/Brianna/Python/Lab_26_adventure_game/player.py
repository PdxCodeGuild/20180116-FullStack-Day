import pygame

import constants

from sprite_objects import ...  # may be a different thing. Sprites? enemies? etc?
from spritesheet_functions import SpriteSheet  # Do I need this if I use individual sprite images I can already list?


class Player(pygame.sprite.Sprite):
    """ This class represents the character that the player controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # -- Attributes
        self.name = "Briar"
        self.max_hit_points = 50
        self.current_hit_points = 50
        self.max_speed = 10
        self.armor_amount = 8
        self.calories = 500

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_u = []
        self.walking_frames_d = []

        # What direction is the player facing?
        self.direction = "R"

        # List of sprites we can bump against
        self.level = None


        # Load all the right facing images, then flip them
        # to face left.
        for images in range(len(self.walking_frames_r)):
            image = pygame.transform.flip(self.walking_frames_r[i], True, False )
            self.walking_frames_l.append(image)

        #  Possibly do the same with images facing up or down?

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        #### should I add things like eat here?

    def update(self):
        """ Move the player. """

        # Move left/right    ##### NEED TO UPDATE THIS FOR MY GAME
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        pos = self.rect.x + self.change_y
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_l[frame]
        elif self.direction == "U":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_u[frame]
        elif self.direction == "D":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_d[frame]

        # See if we hit anything
        border_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False  ## Change to enemies or walls?
        for border in border_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = border.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = border.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        border_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for border in border_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = border.rect.top
            elif self.change_y < 0:
                self.rect.top = border.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(border, MovingPlatform):  ####  AREA TO EDIT. PUT IN ITEMS TO COLLECT AND ENEMY INSTANCES HERE?
                self.rect.x += border.change_x


    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def go_up(self):
        """ Called when the user hits the up arrow. """
        self.change_y = -6
        self.direction = "U"

    def go_down(self):
        """ Called when the user hits the down arrow """
        self.change_y = 6
        self.direction = "D"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
