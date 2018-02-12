import random
import l26_graphics as graphics
from l26_settings import *
from l26_creature import *
from l26_GridCell import *
import pygame, sys


class GameBoard:  # this is what shows up on the screen, 'board' avoids overusing name 'map'
    def __init__(self, width, height): 
        self.board = []  # the grid upon which the screen will be generated
        for y in range(height):  # loop over the rows
            self.board.append([])  # append an empty row
            for x in range(width):  # loop over the columns
                self.board[y].append(' ')  # append an empty space to the board

    def random_board_location(self):  # randomly generated location, conisder revising
        return random.randint(0, BOARD_WIDTH - 1), random.randint(0, BOARD_HEIGHT - 1)

    def __getitem__(self, x):  # lets you call the class within its definition
        return self.board[x]

    def width(self):
        return len(self.board[0])  # __getitem__ allows this to be called explicitly 

    def __getitem__(self, y):
        return self.board[y]

    def height(self):
        return len(self.board)

    def display_creatures(self, creatures, screen):
        origin = [0, 0]
        output_str_list = []
        for y in range(self.height()):
            output_string = ''
            for x in range(self.width()):
                for k in range(len(creatures)):
                    if creatures[k].y_location == y and creatures[k].x_location == x:
                        output_string += (creatures[k].character)
                        break
                else:
                    output_string += (' ')
            output_str_list.append(output_string)
        graphics.set_text(screen, output_str_list, origin)
        graphics.display_screen()

    def make_dungeon(self):
        self.board = [[Wall(y, x) for y in range(BOARD_HEIGHT)] for x in range(BOARD_WIDTH)]

# class Room:  # a rectangular room
#     def __init__(self, x_origin, y_origin, width, height):
#         self.x1 = x_origin
#         self.y1 = y_origin
#         self.x2 = x_origin + width
#         self.y2 = y_origin + height
#
#     def construct_room(self, room):  # make these tiles player passable
#         for x in range(room.x1 + 1, room.x2):
#             for y in range(room.y1 + 1, room.y2):
#                 GameBoard.board[x][y].blocks_path = False
#                 GameBoard.board[x][y].blocks_view = False
#
#     def construct_horz_tunnel(self, x_origin, x_dest, y):
#         for x in range(min(x_origin, x_dest), max(x_origin, x_dest) + 1):
#             GameBoard.board[x][y].blocks_path = False
#             GameBoard.board[x][y].blocks_sight = False
#
#     def construct_vert_tunnel(self, y_origin, y_dest, x):
#         for y in range(min(y_origin, y_dest), max(y_origin, y_dest) + 1):
#             GameBoard.board[x][y].blocks_path = False
#             GameBoard.board[x][y].blocks_sight = False
#
#     def center(self):
#         center_x = (self.x1 + self.x2) // 2
#         center_y = (self.y1 + self.y2) // 2
#         return center_x, center_y
#
#     def intersect(self, other):
#         # returns true if this rectangle intersects with another one
#         return (self.x1 <= other.x2 and self.x2 >= other.x1 and
#                 self.y1 <= other.y2 and self.y2 >= other.y1)


