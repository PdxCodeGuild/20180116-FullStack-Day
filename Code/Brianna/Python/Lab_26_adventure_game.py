import random
import pygame


# ----- OBJECT AND CHARACTER CLASSES IN A SEPARATE SHEET. REFERENCE CODE ALSO MOVED.  ----


# ------------------------------

# ---- A couple of place-holder classes for the moment ----



class Tree(pygame.sprite.Sprite):  # Place holder until I find tree sprites
    """ This class represents a simple block the player collects. """

    def __init__(self):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(SCREEN_WIDTH)

    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 1

        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()

class Enemy(pygame.sprite.Sprite):  # Place holder until I finish defining my enemies, etc.
    def __init__(self):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(SCREEN_WIDTH)

    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 1

        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


class Player(pygame.sprite.Sprite):   # Also a semi-placeholder. Will fill in additional info and possibly separate out into another tab once I finish player attributes.
    """ This class represents the player. """

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def update(self):
        """ Update the player location. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

# ----- Making Game Class --------

class Game(object):
    """ This represents an instance of the Game. By creating this class we can easily reset/restart the game by referencing this instance. """
    # Class attributes and data to run the game
    # Sprites list
    enemies_list = None
    tree_list = None
    all_sprites_list = None
    player = None
    game_over = False

    # other  Data
    score = 0

    """ Class Methods. Setting up the game. """
    def __init__(self):
        self.score = 0
        self.game_over = False

    # Create Sprite lists
        self.enemies_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for i in range(30):
            tree = Tree()


            tree.rect.x = random.randrange(SCREEN_WIDTH)
            tree.rect.y = random.randrange(-300, SCREEN_HEIGHT)

            self.tree_list.add(tree)
            self.all_sprites_list.add(tree)

        for i in range(5):  # Place holder until I figure out how to populate specific screens
            enemy = Enemy()

            enemy.rect.x = random.randrange(SCREEN_WIDTH)
            tree.rect.y = random.randrange(-300, SCREEN_HEIGHT)

        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
                    instruction_page += 1
                elif instruction_page == 3:
                    display_instructions = False

            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT:
                    x_speed = -3
                elif event.key == pygame.K_RIGHT:
                    x_speed = 3
                elif event.key == pygame.K_UP:
                    y_speed = -3
                elif event.key == pygame.K_DOWN:
                    y_speed = 3

            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
        return False


    def run_logic(self):
        """ I should add what happens when colisions occur in here. Update health, etc. Also should add game_over condition """
        if not self.game_over:
            # Move my sprites
            self.all_sprites_list.update()

            # See if player has collided with anything.
            enemy_collision_list = (self.player, self.enemies_list, True)

            # Check the list of collisions
            for enemy in enemy_collision_list:
                self.score += 1  # This is just a place holder until I figure out how to do battles.

            if len(enemy_collision_list) == 0:
                self.game_over = True # Placeholder until I finish my run logic.


    def display_frame(self, screen):
        """ Everything that gets drawn in the game goes here. """
        screen.fill(MID_GREEN)

        def draw_stick_figure(screen, x, y):
            # Head
            pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

            # Legs
            pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
            pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

            # Body
            pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

            # Arms
            pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
            pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

        if game_over:
            # If game over is true, draw game over
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over. Click to restart", True, WHITE)
            text_rect = text.get_rect()
            # Center the text
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text, [text_x, text_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen) # Put what to do here

            for x in range(0, 700, 20):
                pygame.draw.line(screen, MID_GREEN, [x, 0], [x, 500], 10)

                # Move the object according to the speed vector.
                # Speed in pixels per frame
                x_speed = 0
                y_speed = 0

                # Current position
                x_coord = 10
                y_coord = 10

                # Move the object according to the speed vector.
                x_coord = x_coord + x_speed
                y_coord = y_coord + y_speed

                x_coord = x_coord + x_speed
                y_coord = y_coord + y_speed

                draw_stick_figure(screen, x_coord, y_coord)

        pygame.display.flip()


# Call the main function, start up the game


if __name__ == '__main__':
    Main()
