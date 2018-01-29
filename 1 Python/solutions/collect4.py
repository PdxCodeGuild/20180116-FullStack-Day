"""
requirements gathering
7 columns, 6 rows
2 players, red and black take turns adding chips
win condition - 4 in a row, diagonal/vertical/horizontal

design and planning
board - list of lists of ints
    string containing names of colors
player / AI
    players manually entering location (column number)
    dumb AI just make random choices
    v2 - smart AI using min/max state exploration thing
user interface
    draw the board
        add pipes or underscores because a blank board is ambiguous
    prompt the user for the column they want to drop their chip in
    ask them if they want to play again
program architecture
    function to check if a player's won
game mechanics
    win condition - 4 horizontally, vertically, or diagonally
    adding too many pieces for a column
"""

import random


def print_board(board, piece_lookup):
    for j in range(len(board)):
        for i in range(len(board[j])):
            print(piece_lookup[board[j][i]], end='')
        print()


def put_piece(board, column, piece):
    row = 0
    while row < len(board) and board[row][column] == 0:
        row += 1
    row -= 1
    board[row][column] = piece


n_columns = 7
n_rows = 6
piece_lookup = [' ', 'o', 'x']
board = [[0 for j in range(n_columns)] for i in range(n_rows)]

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



print('Welcome to our Collect4™ game')
print(r'''
     .-.
    /'v'\
   (/   \)
  ='="="===< 
  mrf|_|
''')


print('-'*80)

players = [1, 2]
current_player_id = random.randint(0, len(players)-1)

while True:

    print_board(board, piece_lookup)

    while True:
        column = input(f'player {current_player_id}, choose a column (1-{n_columns}): ')
        try:
            column = int(column)
            column -= 1
            if 0 <= column < n_columns:
                break
        except ValueError:
            print('please enter a number')


    piece = current_player_id + 1
    put_piece(board, column, piece)

    current_player_id += 1
    current_player_id %= len(players)



















