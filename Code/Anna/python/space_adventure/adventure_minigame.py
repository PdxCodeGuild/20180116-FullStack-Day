"""
Herding Space Cats

Seriously, that's all this is.

Code borrowed generously from: http://arcade.academy/examples/index.html
Using the arcade library

"""

import random
import arcade
import os

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.25
SPRITE_SCALING_CAT = 0.5
CAT_COUNT = 50
MOVEMENT_SPEED = 5

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640

# These numbers represent "states" that the game can be in.
INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3


class Cat(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the cat
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Herding Space Cats!")

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Background image will be stored in this variable
        self.background = None

        # Start 'state' will be showing the first page of instructions.
        self.current_state = INSTRUCTIONS_PAGE_0

        # Variables that will hold sprite lists
        self.all_sprites_list = None
        self.cat_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

        # STEP 1: Put each instruction page in an image. Make sure the image
        # matches the dimensions of the window, or it will stretch and look
        # ugly. You can also do something similar if you want a page between
        # each level.
        self.instructions = []
        texture = arcade.load_texture("backgrounds/instructions_0.png")
        self.instructions.append(texture)

        texture = arcade.load_texture("backgrounds/instructions_1.png")
        self.instructions.append(texture)

        self.total_time = 0.0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        self.background = arcade.load_texture("backgrounds/background.png")

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.cat_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("spaceships/player_ship.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)

        # Timer
        self.total_time = 0.0

        # Create the coins
        for i in range(50):

            # Create the cat instance
            cat = Cat("spaceships/cat.png", SPRITE_SCALING_CAT)

            # Position the cat
            cat.center_x = random.randrange(SCREEN_WIDTH)
            cat.center_y = random.randrange(SCREEN_HEIGHT)
            cat.change_x = random.randrange(-3, 4)
            cat.change_y = random.randrange(-3, 4)

            # Add the cat to the lists
            self.all_sprites_list.append(cat)
            self.cat_list.append(cat)

    def draw_instructions_page(self, page_number):
        """
        Draw an instruction page. Load the page as an image.
        """
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)

    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "You win! Game Over"
        arcade.draw_text(output, 220, 400, arcade.color.WHITE, 54)

        output = f"Your time was: {round(self.total_time, 2)}"
        arcade.draw_text(output, 350, 300, arcade.color.WHITE, 24)

        output = "Click to restart"
        arcade.draw_text(output, 410, 200, arcade.color.WHITE, 24)

    def draw_game(self):
        """ Draw everything """
        arcade.start_render()
        # # audio theme
        # my_sound = arcade.sound.load_sound('audio/space_cats.wav')
        # arcade.play_sound(my_sound)

        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        # Draw all the sprites
        self.all_sprites_list.draw()

        # Calculate minutes
        minutes = int(self.total_time) // 60

        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60

        # Figure out our output
        timer = f"Time: {minutes:02d}:{seconds:02d}"

        # Put the text on the screen.
        output = f"Cats Herded: {self.score}"
        arcade.draw_text(output, 10, 40, arcade.color.GHOST_WHITE, 14)
        arcade.draw_text(timer, 10, 20, arcade.color.GHOST_WHITE, 14)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)

        elif self.current_state == INSTRUCTIONS_PAGE_1:
            self.draw_instructions_page(1)

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        else:
            self.draw_game()
            self.draw_game_over()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change states as needed.
        if self.current_state == INSTRUCTIONS_PAGE_0:
            # Next page of instructions.
            self.current_state = INSTRUCTIONS_PAGE_1
        elif self.current_state == INSTRUCTIONS_PAGE_1:
            # Start the game
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            # Restart the game.
            self.setup()
            self.current_state = GAME_RUNNING

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """
        if self.current_state == GAME_RUNNING:
            # Call update on all sprites
            self.all_sprites_list.update()

            # update the timer
            self.total_time += delta_time

            # Generate a list of all sprites that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.cat_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for cat in hit_list:
                cat.kill()
                self.score += 1

            # If we've collected all the cats, then move to a "GAME_OVER"
            # state.
            if len(self.cat_list) == 0:
                self.current_state = GAME_OVER
                self.set_mouse_visible(True)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
