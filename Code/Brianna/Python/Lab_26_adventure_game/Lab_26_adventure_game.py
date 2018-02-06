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
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

"""


"""


pygame.init()


# ----- Global constants -----

#         R    G    B
WHITE = (255, 255, 255)
MID_GREEN = (0, 135, 27)
FOREST_GREEN = (1, 96, 20)
LEAF_GREEN = (15, 198, 5)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# ------------------------------

# Set font
font = pygame.font.Font(None, 36)
# Set width and height of the screen. First number is width, second is height.
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size) # can put size directly in (size) area. Screen is the variable name we have assigned this window to. We can create more windows.

pygame.display.set_caption("Programmer's Escape to Hidden Mountain")

# Loop until the user clicks the close button.
done = False  # Loop control

# Used to manage how fast the screen updates
clock = pygame.time.Clock()  # Controls how fast the game runs

'''
# Make an image follow the cursor around. Need to have an image file here.
cursor_picture = pygame.image.load('./cursor.png').convert_alpha()'''

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

""""# Need to download from http://freemusicarchive.org/music/MIT_Concert_Choir and put in folder to point to.
pygame.mixer.music.load('MIT_Concert_Choir_O_Fortuna.ogg')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

# This is a font we use to draw text on the screen (size 36)
#font = pygame.font.Font(None, 36)"""


""""# Use this boolean variable to trigger if the game is over.
game_over = False
    if game_over:
        # If game over is true, draw game over
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
 """

display_instructions = True
instruction_page = 1

# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False

    # Set the screen background
    screen.fill(BLACK)

    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.

        text = font.render("Welcome to Escape to Code Mountain", True, WHITE)
        screen.blit(text, [10, 10])

        text = font.render("Page 1", True, WHITE)
        screen.blit(text, [10, 40])

    if instruction_page == 2:
        # Draw instructions, page 2
        text = font.render("This program has instructions. Hopefully they aren't complicated. ", True, WHITE)
        screen.blit(text, [10, 10])

        text = font.render("Page 2", True, WHITE)
        screen.blit(text, [10, 40])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

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

        elif event.type == pygame.constants.USEREVENT:
            # This event is triggered when the song stops playing.
            #
            # Next, play "Alone" by Saito Koji
            # Available from:
            # http://freemusicarchive.org/music/Saito_Koji/Again/01-Alone
            pygame.mixer.music.load('Saito_Koji_-_01_-_Alone.ogg')
            pygame.mixer.music.play()



    # --- Game logic should go here

    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed


    # --- Drawing code should go here

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    #text = font.render("Score: " + str(score), True, black)

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(LEAF_GREEN)
    for x in range(0, 700, 20):
        pygame.draw.line(screen, MID_GREEN, [x, 0], [x, 500], 10)

    # Putting the mouse on the screen?
    #screen.blit(mouse_cursor, pygame.mouse.get_pos())
    #pygame.display.update()

    draw_stick_figure(screen, x_coord, y_coord)
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