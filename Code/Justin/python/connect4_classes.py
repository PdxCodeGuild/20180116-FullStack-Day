"""Connect 4 using a Board class"""

import random
import itertools


class Board():
    """ This is the game board, stores number of rows, number of columns
    :var status is a dictionary of each board location (0 if empty, player number if occupied
    :var column_spaces is dictionary, {column numbers: number of spaces left in column}
    :var column_labels_string is a string of the form '   1   2   3   4... ' for top of board"""

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        # self.status initializes entire to a dictionary {(i, j): 0},
        # keys are made from a dictionary comprehension (cartesian product of rows numbers and columns numbers)
        self.status = dict((location, 0) for location in
                    sorted(itertools.product([i for i in range(1, rows + 1)], [j for j in range(1, columns + 1)])))
        # self.column_spaces initializes to dictionary, one key for each column, values initialize to number of rows
        self.column_spaces = dict((i, rows) for i in range(1, columns+1))
        self.column_labels_string = '  ' + '   '.join([str(i) for i in range(1, columns+1)])


    def __str__(self):
        """This builds one long string consisting of column numbers, and each row of playing board"""

        pieces = [' ', 'X', 'O', '$'] # 0 is empty, player 1 gets X, player 2 gets O, winning sequences get '$'
        board_string = self.column_labels_string + '\n'
        board_string = board_string + '-' + ('----' * self.columns) + '\n'
        for i in range(1, self.rows+1):
            for j in range(1, self.columns+1):
                board_string = board_string + '| ' + pieces[board.status[(i, j)]] + ' '
            board_string = board_string + '|\n'
            board_string = board_string + '-' + ('----' * self.columns) + '\n'
        return board_string

    def get_rows(self):
        """returns the number of rows in the board"""
        return self.rows

    def get_columns(self):
        """returns the number of columns in the board"""
        return self.columns

    def get_status(self, i, j):
        """return the value stored in space (i, j), 0 is empty, 1 or 2 for player number, 3 if part of a winning sequence"""
        return self.status[(i, j)]

    def change_status(self, j, k, m):
        """changes the values stored at location (j, k) to m 0 is empty, 1 or 2 for player, 3 for part of a winning sequence"""
        self.status[(j, k)] = m

    def get_spaces(self, i):
        """returns the number of spaces left in column i"""
        return self.column_spaces[i]

    def change_spaces(self, i):
        """lowers the number of spaces left in a column by 1 when a player chooses to play that column"""
        self.column_spaces[i] -= 1

    def spaces_left(self):
        """returns the total number of spaces left, returns 0 when the board is full. This is just check for a full board"""
        return sum(list(self.column_spaces.values()))




def choose_column(player_number):
    """players choose columns or computer makes random choices
    depending on value of random_play

    :param player_number is the player number
    :returns integer between 1 and number of columns"""

    if random_play:
        choice = random.randint(1, board.get_columns())
        print(f'Player {player_number} chooses column {choice}')
        while board.get_spaces(choice) == 0:
            print('That column is full, try again: ')
            choice = random.randint(1, board.get_columns())
            print(f'Player {player_number} chooses column {choice}')
        return choice
    else:
        choice = int(input(f'Player {player_number} enter a column: '))
        while board.get_spaces(choice) == 0:
            choice = int(input('That column is full, try again: '))
        return choice



def check_win(player_number):
    """check for win, this function is called after every player mainLoop
    checks for vertical, horizontal and two diagonal directions separately

    :param player_number is the players's number
    :returns boolean True for win"""

    # Check for vertical win
    for i in range(1, board.get_rows() + 1 - 3):
        for j in range(1, board.get_columns() + 1):
            if board.get_status(i, j) == board.get_status(i+1, j) == \
                    board.get_status(i+2, j) == board.get_status(i+3, j) == player_number:
                for k in range(4):
                    board.change_status(i + k, j, 3)
                return True

    # Check for horizontal win
    for i in range(1, board.get_rows() + 1):
        for j in range(1, board.get_columns() + 1 - 3):
            if board.get_status(i, j) == board.get_status(i, j + 1) == \
                    board.get_status(i, j + 2) == board.get_status(i, j + 3) == player_number:
                for k in range(4):
                    board.change_status(i, j + k, 3)
                return True

    # Check for diagonal down (\) win
    for i in range(1, board.get_rows() + 1 - 3):
        for j in range(1, board.get_columns() + 1 - 3):
            if board.get_status(i, j) == board.get_status(i + 1, j + 1) == \
                    board.get_status(i + 2, j + 2) == board.get_status(i + 3, j + 3) == player_number:
                for k in range(4):
                    board.change_status(i + k, j + k, 3)
                return True

    # Check for diagonal up (/) win
    for i in range(4, board.get_rows() + 1):
        for j in range(1, board.get_columns() + 1 - 3):
            if board.get_status(i, j) == board.get_status(i - 1, j + 1) == \
                    board.get_status(i - 2, j + 2) == board.get_status(i - 3, j + 3) == player_number:
                for k in range(4):
                    board.change_status(i - k, j + k, 3)
                return True

    return False


# Initialize board and game variables
board = Board(6, 7)
number_of_players = 2
results = [False for i in range(number_of_players+1)] # results[0] stores full board boolean
print(board)




# Start Game
print('Lets play Connect4!!!')
random_play = False

while True:

    for i in range(1, number_of_players+1):
        # Player chooses column
        choice = choose_column(i)

        # Board status is updated, location (board.get_spaces(choice), choice) gets value equal to i (player number)
        board.change_status(board.get_spaces(choice), choice, i)
        # Update the number of spaces left in that column
        board.change_spaces(choice)

        # Check if player number i has a win
        results[i] = check_win(i)

        # Print the board
        print(board)

        # Print *'s for clarity
        print('*' * 50)

    # Check for a full board
    if board.spaces_left() == 0:
        results[0] = True

    # Check for end of game (full board or winner)
    if True in results:
        break

# Print results of game
if results[0]:
    print("The board is full, Game Over!")

if False not in results[1:]:
    print('Everybody wins!!!')

if results[1]:
    print('Player 1 wins!')

if results[2]:
    print('Player 2 wins!')




