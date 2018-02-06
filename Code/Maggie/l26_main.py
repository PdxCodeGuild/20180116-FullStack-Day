import random
import l26_graphics as graphics
import l26_settings as settings
from l26_gameboard import *
from l26_creature import *
import pygame, sys

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
    elif key == 'q':
        pygame.QUIT = True

def update_game():
    move_choices = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    for character in npcs:
        character.move(random.choice(move_choices))


def initialize_game():  # loading settings into memory
    pygame.font.init()
    pygame.display.init()

    pygame.event.clear()    #event queue settings
    pygame.event.set_allowed(None)
    pygame.event.set_allowed(pygame.KEYDOWN)
    pygame.event.set_allowed(pygame.QUIT)

def run_main_loop():
    sys_clock = pygame.time.Clock()  # to keep CPU usage down
    message_box.messages.append('Adventure!')
    while True:
        screen.fill((0, 0, 0))
        board.display_creatures(creatures, screen)
        message_box.display_message()
        graphics.display_screen()
        events = pygame.event.get()
        for event in events:
            message_box.message = ''
            if event.type == pygame.KEYDOWN:
                handle_keypress(event.key)
                print(event.key)
            if event.type == pygame.QUIT:
                pygame.quit()
        update_game()
        sys_clock.tick(30)

# INITIAL STATES
board = GameBoard(32, 16)  # the board upon which to generate the game
py, px = board.random_location()
player = Player(py, px)
creatures = [player]
npcs = []
screen = graphics.init_screen('ADVENTURE', settings.pi_img, settings.SCREEN_SIZE)

message_box = graphics.MessageBox(screen)  # instance of MessageBox
status_box = graphics.StatusBox(screen)

for i in range(10):
    ry, rx = board.random_location()
    npc = NPC(ry, rx)
    creatures.append(npc)
    # creatures.append(npc)


# RUN GAME
initialize_game()
run_main_loop()


