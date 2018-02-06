import random
import l26_graphics as graphics
import l26_settings as settings
import pygame, sys

class GridCell:

class GameBoard:  # this is what shows up on the screen, 'board' avoids overusing name 'map'
    def __init__(self, width, height): 
        self.board = []  # the grid upon which the screen will be generated
        for i in range(height):  # loop over the rows
            self.board.append([])  # append an empty row
            for j in range(width):  # loop over the columns
                self.board[i].append(' ')  # append an empty space to the board

    def random_location(self):  # randomly generated location, conisder revising
        return random.randint(0, self.width() - 1), random.randint(0, self.height() - 1)

    def __getitem__(self, j):  # lets you call the class within its definition
        return self.board[j]

    def width(self):
        return len(self.board[0])  # __getitem__ allows this to be called explicitly 

    def height(self):
        return len(self.board)

    def display_creatures(self, creatures, screen):
        origin = [0, 0]
        output_str_list = []
        for i in range(self.height()):
            output_string = ''
            for j in range(self.width()):
                for k in range(len(creatures)):
                    if creatures[k].y_location == i and creatures[k].x_location == j:
                        output_string += (creatures[k].character)
                        break
                else:
                    output_string += ('.')
            output_str_list.append(output_string)
        graphics.set_text(screen, output_str_list, origin)
        graphics.display_screen()

    def make_gameboard(self):
        pass

