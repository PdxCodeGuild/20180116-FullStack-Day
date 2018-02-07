
from random import randint

def print_board(board, piece_lookup):
    for j in range(len(board)):
        for i in range(len(board[j])):
            print(piece_lookup[board[j][i]], '|', end='')
        print()  # starts a new row


def put_piece(board, column, piece):
    row = 0
    while row < len(board) and board[row][column] == 0:
        row += 1
    row -= 1
    board[row][column] = piece


n_rows = 6
n_columns = 7
piece_lookup = ['_', 'o', 'x']
board = [[0 for j in range(n_columns)] for i in range(n_rows)]


players = [1, 2]
current_player_id = randint(0, len(players) -1)

while True:
    print_board(board, piece_lookup)
    column = input(f'Player {current_player_id}, choose a column (1-{n_columns}): ')
    try:
        column = int(column)
        column -= 1
        if column < 0 and column <= n_columns:
            break
    except ValueError:
        print('please enter a valid number.')

    piece = current_player_id + 1
    put_piece(board, column, piece)

    # current_player_id += 1
    # current_player_id %= len(players)
