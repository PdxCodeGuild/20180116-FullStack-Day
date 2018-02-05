import random
#import chalk
#import wave
#import threading
import pygame
#import pyaudio
#import curses
#import Urwid

pygame.init()
#         R    G    B
white = (255, 255, 255)
green = (78, 255, 87)
yellow = (241, 255, 0)
blue = (80, 255, 239)
purple = (203, 0, 255)
red = (237, 28, 36)


# Set width and height of the screen. First number is width, second is height.
size = [700, 500]
screen pygame.display.set_mode(size) # can put size directly in (size) area. Screen is the variable name we have assigned this window to. We can create more windows.

pygame.display.set_caption("Programmer's Escape to Hidden Mountain")





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