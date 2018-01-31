"""
Let's play Collect Four!

# requirements gathering
7 columns, 6 rows
2 players, red and black, take turns adding chips
win condition - 4 in a row, diagonal/vertical/horizontal

# design and planning
board: list of lists of ints
    string containing names of colors
player representation:
    players manually entering location (column name)
    dumbAI just make random choices
    v2 - smart AI using min/max state exploration?
user interface:
    draw the board
        add pipes or underscores so board not blank
    prompt the user for the column they want to drop their chip in
    ask them if they want to play again
program architecture:
    function to check if a player's won
game mechanics:
    win condition
    adding too many pieces for a column
    fail condition (if board full without win)
"""

import random


class Collect4:
    """This is totally not a Collect 4™ rip-off. Milton Bradley, please don't sue us."""

    def __init__(self, n_columns, n_rows, n_pieces_to_win):
        """Initialize!"""
        self.n_columns = n_columns
        self.n_rows = n_rows
        self.n_pieces_to_win = n_pieces_to_win

    def print_board(self, board, piece_lookup):
        for j in range(len(board)):
            for i in range(len(board[j])):
                print(piece_lookup[board[j][i]], end='')
            print()
        print("  " + '    '.join([str(i) for i in range(1, len(board[0]) + 1)]))

    def put_piece(self, board, column, piece):
        row = 0
        while row < len(board) and board[row][column] == 0:
            row += 1
        row -= 1
        if row > -1:
            board[row][column] = piece
            return True
        return False

    def column_full(self, board, column):
        return board[0][column] != 0

    def all_columns_full(self, board):
        for column in range(len(board[0])):
            if not self.column_full(board, column):
                return False
        return True

    def check_direction(self, board, piece, row, column, row_increment, column_increment):
        for i in range(self.n_pieces_to_win):
            if row >= len(board) or column >= len(board[row]):
                return False
            if board[row][column] != piece:
                return False
            row += row_increment
            column += column_increment
        return True

    def check_all_directions(self, board, piece, row, column):
        direction_values = [-1, 0, 1]
        for d0 in direction_values:
            for d1 in direction_values:
                if d0 == 0 and d1 == 0:
                    continue
                if self.check_direction(board, piece, row, column, d0, d1):
                    return True
        return False

    def check_win(self, board):
        for row in range(len(board)):
            for column in range(len(board[row])):
                piece = board[row][column]
                if piece == 0:
                    continue
                if self.check_all_directions(board, piece, row, column):
                    return True
        return False


print('\nWelcome to our Collect4™ game')
print(r'''
             .-.
            /'v'\
           (/   \)
          ='="="===< 
             |_|
''')


print('-'*80)

my_game = Collect4(7, 6, 4)

piece_lookup = ['[___]', '[ o ]', '[ x ]']
board = [[0 for j in range(my_game.n_columns)] for i in range(my_game.n_rows)]

players = [1, 2]
current_player_id = random.randint(0, len(players)-1)


while True:

    my_game.print_board(board, piece_lookup)

    while True:
        if current_player_id == 0:
            column = input(f'player {current_player_id}, choose a column (1-{my_game.n_columns}): ')
        elif current_player_id == 1:
            column = random.randint(1, my_game.n_columns+1)
            print(f"The computer chooses {column}.")
        try:
            column = int(column)
            column -= 1
            if column < 0 or column >= my_game.n_columns:
                print("That is not a column in range")
            elif my_game.column_full(board, column):
                print("That column is full")
            else:
                break
            if 0 <= column < my_game.n_columns and not my_game.column_full(board, column):
                break
        except ValueError:
            print('Not a valid number')

    piece = current_player_id + 1
    my_game.put_piece(board, column, piece)

    if my_game.all_columns_full(board):
        my_game.print_board(board, piece_lookup)
        print("All columns full with no winner. Game over!")
        break
    if my_game.check_win(board):
        my_game.print_board(board, piece_lookup)
        print(f"Game over! Player {current_player_id} is the winner!")
        break

    current_player_id += 1
    current_player_id %= len(players) # go to the first player when we go past the end
