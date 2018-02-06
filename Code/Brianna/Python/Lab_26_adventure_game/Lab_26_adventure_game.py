import random
#import chalk
#import wave
#import threading
import pygame
#import pyaudio
#import curses
#import Urwid



def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, black, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, black, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, black, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, red, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, red, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, red, [5 + x, 7 + y], [1 + x, 17 + y], 2)

class Character():
    """ This is a class that represents the main character in a game. """

    def __init__(self):
        """ Setting up a starting point for our character """
        self.name = "Briar"
        self.max_hit_points = 50
        self.current_hit_points = 50
        self.max_speed = 10
        self.armor_amount = 8
        self.calories = 500

    def eat(self, calories):
        self.calories += calories
        return self.calories

    def sleep(self, sleep=100):
        if sleep == 100:
            self.max_hit_points = 50
        return

    def attack(self):
        pass

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


class Cave_monster(Enemies):  # Common and can move around. You can see them before you run into them.
    pass


class Bandit(Enemies):  # Uncommon and you cannot see them unless you run into them. Possibly move around.
    pass


class Found_items():   # Found items can be put into a sack/inventory and used later.
    """ This class sets up the kinds of items our main character can pick up"""
    def __init__(self, name):
        self.name = name
        self.place_in_sack = True
        self.used = False



class Food():
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
        self.place_in_sack = True
        self.used = False


ham = Food('ham', 230)
casserole = Food('casserole', 100)
can_of_soup = Food('can of soup', 50)




pygame.init()
#         R    G    B
white = (255, 255, 255)
mid_green = (0, 135, 27)
forest_green = (1, 96, 20)
leaf_green = (15, 198, 5)
yellow = (241, 255, 0)
blue = (80, 255, 239)
purple = (203, 0, 255)
red = (237, 28, 36)


# Set width and height of the screen. First number is width, second is height.
size = [700, 500]
screen = pygame.display.set_mode(size) # can put size directly in (size) area. Screen is the variable name we have assigned this window to. We can create more windows.

pygame.display.set_caption("Programmer's Escape to Hidden Mountain")

# Loop until the user clicks the close button.
done = False  # Loop control

# Used to manage how fast the screen updates
clock = pygame.time.Clock()  # Controls how fast the game runs

'''# Make the cursor transparent.
mouse_cursor = pygame.mouse.set_cursor(pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0)))

# Make an image follow the cursor around. Need to have an image file here.
cursor_picture = pygame.image.load('./cursor.png').convert_alpha()'''

# Hide the mouse cursor
pygame.mouse.set_visible(0)



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.get_pos()
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pygame.mouse.get_pos()
            pass
        elif event.type == pygame.MOUSEMOTION:
            pygame.mouse.set_visible(True)
            pygame.mouse.get_pos()
            pass



    # --- Game logic should go here




    # --- Drawing code should go here

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text = font.render("Score: " + str(score), True, black)

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(leaf_green)
    for x in range(0, 700, 20):
        pygame.draw.line(screen, mid_green, [x, 0], [x, 500], 10)

    # Putting the mouse on the screen?
    screen.blit(mouse_cursor, pygame.mouse.get_pos())
    pygame.display.update()
    # ---  update the screen with what we've drawn.
    pygame.display.flip() # Like a flip book. Flips things to the screen. Do after drawing.

    # --- Limit to 60 frames per second
    clock.tick(60)  # Only want one of these in main program loop. It should be at the end.

pygame.quit()


"""


class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class Tree(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, 'Ѧ')


class Enemy(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '§')


class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '☺')


class Board:
    def __init__(self, width, height):
        self.board = []
        for i in range(height):  # loop over the rows
            self.board.append([])  # append an empty row
            for j in range(width):  # loop over the columns
                self.board[i].append('x')  # append an empty space to the board

    def random_location(self):
        return random.randint(0, self.width() - 1), random.randint(0, self.height() - 1)

    def __getitem__(self, j):
        return self.board[j]

    def width(self):
        return len(self.board[0])

    def height(self):
        return len(self.board)

    def print(self, entities):
        for i in range(self.height()):
            for j in range(self.width()):
                for k in range(len(entities)):
                    if entities[k].location_i == i and entities[k].location_j == j:
                        print(entities[k].character, end='')
                        break
                else:
                    print(' ', end='')
            print()



b = Board(10, 10)

pi, pj = b.random_location()
player = Player(pi, pj)

entities = [player]
enemies = []

for i in range(10):
    ei, ej = b.random_location()
    enemy = Enemy(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)


while True:

    b.print(entities)

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'left':
        player.location_j -= 1  # move left
    elif command == 'right':
        player.location_j += 1  # move right
    elif command == 'up':
        player.location_i -= 1  # move up
    elif command == 'down':
        player.location_i += 1  # move down

    for enemy in enemies:
        if random.randint(0, 1) == 0:
            enemy.location_i += random.randint(-1, 1)
        else:
            enemy.location_j += random.randint(-1, 1)

"""