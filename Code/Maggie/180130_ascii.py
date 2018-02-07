import string

class Tile:
    rows = 32
    columns = 32
    field = [[0 for j in range(32)] for i in range(32)]

    def __init__(self, character, row, column):
        self.character = character
        self.row = row
        self.column = column

    def tile_character(self, char_index= 0):
        character_string = (string.printable)
        self.character = character_string[char_index]

    def print_field(self):
        for j in range(len(self.field)):
            for i in range(len(self.field[j])):
                print(self.tile_character()[self.field[j][i]], ' ', end='')
            print()  # starts a new row

test_tile = Tile(0,16,16)
Tile.print_field(test_tile)

