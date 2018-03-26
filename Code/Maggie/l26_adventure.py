# Adventure game
from __future__ import print_function
from blessed import Terminal
import adv_keypress as k
from random import choice
# Display parameters
t = Terminal
width = 10  # the width of the board
height = 10  # the height of the board
tiles = ['.', '@', '#', '*', '$', '!', '~', '§']
int_board = [[0 for j in range(height)] for i in range(width)]  # init the empty int_board
# int_board[3][3] = 1


# Organizing game elements into classes
class BoardSpot:  # properties of cells within the play area
    def __init__(self, impassable, seen, occupied, blocks_view):
        self.impassable = impassable  # blocks movement
        self.seen = seen  # is this currently visible to player?
        self.explored = False  # all spots start unexplored
        if self.seen:
            self.explored = True  # if the player is seeing it, then it's explored
        self.occupied = occupied  # is there anything in this cell?
        self.blocks_view = blocks_view  # does the occupant block view

class GamePiece:  # all of the tilebased game elements, including the player
    def __init__(self, y_loc, x_loc, char_int, name):
        self.y_loc = y_loc
        self.x_loc = x_loc
        self.ascii_char = char_int
        self.name = name

    def move(self, dx, dy):  # mainLoop a piece by an amount
        self.x_loc += dx
        self.y_loc += dy

    def put_on_int_board():
        for pieces in game_pieces: # add the piece to the int_board
            int_board[y][x] = char_int

    def clear_spot(self, x, y):
        int_board[y][x] = 0

class Person:
    names = ['mike', 'vere', 'marcy', 'kim', 'joy', 'mildred', 'marty', 'Jeff', 'Manny', 'megan', 'mad max', 'Moore',
             'junior', 'Minty', 'myspace tom', 'Hugh Jass', 'john', 'jacob', 'jingleheimer', 'smith', 'Morticia',
             'Rick', 'Morty', 'jon smith', 'not sure', 'Beef Supreme', 'Mob', 'Toffle', 'moore']

    def __init__(self):
        self.energy = 5
        self.items = []
        self.name = choice(self.names)

    def __str__(self): # if the piece is called in a print statement
        return(self.name)


player_piece = GamePiece(3, 3, 1, 'Player')
game_pieces = [player_piece]



def main():
    message = 'Adventures in development.'
    status = 'hello testphrase.'
    escaped = False
    while not escaped:  # main game loop
        key_log = []
        key_press = k.handle_keys() # get the keypress
        GamePiece.put_on_int_board()
        # do all the updates..
        print_game_board(int_board, tiles)

def print_game_board(int_board, tile_set):

    for i in range(len(int_board)):
        for j in range(len(int_board[i])):  # in the
            print(tile_set[int_board[i][j]], ' ', end='')
        print()

main()