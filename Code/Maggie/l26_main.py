import random
from l26_gameboard import *
from l26_graphics import *
from l26_creature import *
from l26_GridCell import *
import pygame, sys

MAIN_CONSOLE = init_screen()
def handle_keypress(key):
    if key == pygame.K_UP:
        player.move(0, -1)
        message_box.messages.append('you pressed up.')
    elif key == pygame.K_DOWN:
        player.move(0, 1)
        message_box.messages.append('you pressed down.')
    elif key == pygame.K_LEFT:
        player.move(-1, 0)
        message_box.messages.append('you pressed left.')
    elif key == pygame.K_RIGHT:
        player.move(1, 0)
        message_box.messages.append('you pressed right.')
    elif key == pygame.K_q:
        message_box.messages.append('Quit.')
        pygame.QUIT = True
        terminate()

def update_game():
    move_choices = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    for character in npcs:
        if random.randint(0, 1) == 0:
            character.y_location += random.randint(-1, 1)
        else:
            character.x_location += random.randint(-1, 1)


def terminate():  # termination
    pygame.quit()  # pygame's controlled termination handler
    sys.exit

def initialize_game():  # loading settings into memory
    pygame.font.init()
    pygame.display.init()

    pygame.event.clear()    #event queue settings
    pygame.event.set_allowed(None)
    pygame.event.set_allowed(pygame.KEYDOWN)
    pygame.event.set_allowed(pygame.QUIT)

def run_main_loop():
    escaped = False
    sys_clock = pygame.time.Clock()  # to keep CPU usage down
    message_box.messages.append('Adventure!')
    while not escaped:
        MAIN_CONSOLE.fill((0, 0, 0))
        update_game()
        board.display_creatures(creatures, MAIN_CONSOLE)
        message_box.display_message()
        graphics.display_screen()
        events = pygame.event.get()
        for event in events:
            message_box.message = ''
            if event.type == pygame.KEYDOWN:
                handle_keypress(event.key)
            if event.type == pygame.QUIT:
                escaped = True
                terminate()

        sys_clock.tick(30)
    terminate()

# INITIAL STATES
#Main surface for terminal display
board = GameBoard(BOARD_WIDTH, BOARD_HEIGHT)  # the board upon which to generate the game
# board.make_dungeon()
py, px = board.random_board_location()
player = Player(px, py)
creatures = [player]
npcs = []

message_box = graphics.MessageBox(MAIN_CONSOLE)  # instance of MessageBox
status_box = graphics.StatusBox(MAIN_CONSOLE)

for i in range(10):
    ry, rx = board.random_board_location()
    npc = NPC(ry, rx)
    creatures.append(npc)
    # creatures.append(npc)

if __name__ == '__main__':
    # RUN GAME
    initialize_game()
    run_main_loop()


# object assembly