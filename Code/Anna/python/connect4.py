"""
Let's play Connect Four!

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


def print_board(board, piece_lookup):
    for j in range(len(board)):
        for i in range(len(board[j])):
            print(piece_lookup[board[j][i]], end='')
        print()
    print(" " + '  '.join([str(i) for i in range(1, len(board[0]) + 1)]))


def put_piece(board, column, piece):
    row = 0
    while row < len(board) and board[row][column] == 0:
        row += 1
    row -= 1
    if row > -1:
        board[row][column] = piece
        return True
    return False


def column_full(board, column):
    return board[0][column] != 0


def all_columns_full(board):
    for column in range(len(board[0])):
        if not column_full(board, column):
            return False
    return True


def check_direction(board, piece, row, column, row_increment, column_increment):
    for i in range(n_pieces_to_win):
        if row >= len(board) or column >= len(board[row]):
            return False
        if board[row][column] != piece:
            return False
        row += row_increment
        column += column_increment
    return True


def check_all_directions(board, piece, row, column):
    direction_values = [-1, 0, 1]
    for d0 in direction_values:
        for d1 in direction_values:
            if d0 == 0 and d1 == 0:
                continue
            if check_direction(board, piece, row, column, d0, d1):
                return True
    return False



def check_win(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            piece = board[row][column]
            if piece == 0:
                continue
            if check_all_directions(board, piece, row, column):
                return True
    return False



n_columns = 7
n_rows = 6
piece_lookup = [' _ ', ' o ', ' x ']
board = [[0 for j in range(n_columns)] for i in range(n_rows)]
n_pieces_to_win = 4

# alternative way of generating the board
# board = []
# for i in range(n_rows):
#     board.append([])
#     for j in range(n_columns):
#         board[i].append(0)

# testing stuff
# for i in range(20):
#     piece = random.randint(1, 2)
#     column = random.randint(0, len(board[0])-1)
#     put_piece(board, column, piece)


print('\nWelcome to our Collect4™ game')
print(r'''
     .-.
    /'v'\
   (/   \)
  ='="="===< 
     |_|
''')


print('-'*80)

players = [1, 2]
current_player_id = random.randint(1, len(players))

while True:

    print_board(board, piece_lookup)

    while True:
        column = input(f'player {current_player_id}, choose a column (1-{n_columns}): ')
        try:
            column = int(column)
            column -= 1
            if column < 0 or column >= n_columns:
                print("That is not a column in range")
            elif column_full(board, column):
                print("That column is full")
            else:
                break
            if 0 <= column < n_columns and not column_full(board, column):
                break
        except ValueError:
            print('Not a valid number')

    piece = current_player_id + 1
    put_piece(board, column, piece)

    if all_columns_full(board):
        print_board(board, piece_lookup)
        print("All columns full with no winner. Game over!")
        break
    if check_win(board):
        print_board(board, piece_lookup)
        print(f"Game over! Player {current_player_id} is the winner!")
        break

    current_player_id += 1
    current_player_id %= len(players)