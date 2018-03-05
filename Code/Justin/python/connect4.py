import random



def initialize_board():
    board = []
    for i in range(board_height):
        board.append([])
        for j in range(board_width):
            board[i].append(0)
    return board

def draw_board(board, board_height = 6, board_width = 7):
    column_lables_string = ' '
    for i in range(board_width):
        column_lables_string = column_lables_string + ' ' + str(i+1) + '  '
    print(column_lables_string)
    print('----'*7 + '-')
    for i in range(board_height):
        for j in range(board_width):
            print('| ' + pieces[board[i][j]] + ' ', end = '')
        print('|')
        print('----' * 7 + '-')

def choose_column(player_number, board_width, column_spaces):
    # choice = int(input(f'Player {player_number} enter a column: '))
    # column_index = choice - 1
    column_index = random.randint(0, board_width-1)
    print(f'Player {player_number} chooses column {column_index+1}')
    while column_spaces[column_index] == 0:
        # choice = int(input('That column is full, try again: '))
        # column_index = choice - 1
        print('That column is full, try again: ')
        column_index = random.randint(0, board_width - 1)
        print(f'Player {player_number} chooses column {column_index+1}')

    row_index = column_spaces[column_index]-1
    column_spaces[column_index] = row_index
    return row_index, column_index, column_spaces

def update_board(board, player_number, row, column):
    board[row][column] = player_number
    return board

def check_win(player_number, board):
    # Check for vertical win
    for i in range(board_height - 3):
        for j in range(board_width):
            if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] == player_number:
                #board[i][j] = board[i + 1][j] = board[i + 2][j] = board[i + 3][j] = 3
                return True

    # Check for horizontal win
    for i in range(board_height):
        for j in range(board_width - 3):
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == 1:
                #board[i][j] = board[i][j + 1] = board[i][j + 2] = board[i][j + 3] = 3
                return True

    # Check for diagonal down win
    for i in range(board_height - 3):
        for j in range(board_width - 3):
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == 1:
                #board[i][j] = board[i + 1][j + 1] = board[i + 2][j + 2] = board[i + 3][j + 3] = 3
                return True

    # Check for diagonal up win
    for i in range(3, board_height):
        for j in range(board_width - 3):
            if board[i][j] == board[i - 1][j + 1] == board[i - 2][j + 2] == board[i - 3][j + 3] == 1:
                #board[i][j] = board[i - 1][j + 1] = board[i - 2][j + 2] = board[i - 3][j + 3] = 3
                return True

    return False


# Initialize Game Variables
board_height = 6
board_width = 7
number_of_players = 2
pieces = [' ', 'X', 'O', '$']
column_spaces = [board_height for i in range(board_width)] # This list records number of open spaces in each colum
results = [False for i in range(number_of_players+1)] # results[0] stores full board boolean



# Initialize game play
print('Lets play Connect4!!!')
input()
board = initialize_board()
draw_board(board, board_height, board_width) # Draw initial board


# Start Game
while True:

    for i in range(1, number_of_players+1):
        row, column, column_spaces = choose_column(i, board_width, column_spaces)

        board = update_board(board, i, row, column)
        draw_board(board, board_height, board_width)

        results[i] = check_win(i, board)
        input()
        print('*' * 50)

    # Check for a full board
    if sum(column_spaces) == 0:
        results[0] = True

    if True in results:
        break

if results[0]:
    print("The board is full, Game Over!")

if results[1]:
    print('Player 1 wins!')
if results[2]:
    print('Player 2 wins!')

