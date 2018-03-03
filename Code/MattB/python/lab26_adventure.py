import random

width = 10  # the width of the board
height = 10  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4

have_weapon = 0

# Add weapon in random spot
weapon_i = random.randint(0, height - 1)
weapon_j = random.randint(0, width - 1)
board[weapon_i][weapon_j] = '?'

# add user amount of enemies in random locations
enemies = input("Input number of enemies: ")

# Set designated number of enemies randomly on the board
for i in range(int(enemies)):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

# Randomly move enemies each turn
def enemy_move(a_board):
    for i in range(height):
        for j in range(width):
            if a_board[i][j] == '§':
                move = random.randint(0, 4)
                if move == 1 and j != 0:                    # left
                    a_board[i][j] = ' '
                    a_board[i][j - 1] = '§'
                elif move == 1 and j == 0:                  # left
                    a_board[i][j] = ' '
                    a_board[i][width - 1] = '§'
                elif move == 2 and j != width - 1:          # right
                    a_board[i][j] = ' '
                    a_board[i][j + 1] = '§'
                elif move == 2 and j == width - 1:
                    a_board[i][j] = ' '
                    a_board[i][0] = '§'
                elif move == 3 and i != 0:                  # up
                    a_board[i][j] = ' '
                    a_board[i - 1][j] = '§'
                elif move == 3 and i == 0:  # up
                    a_board[i][j] = ' '
                    a_board[height - 1][j] = '§'
                elif move == 4 and i != height - 1:         # down
                    a_board[i][j] = ' '
                    a_board[i + 1][j] = '§'
                elif move == 4 and i == height - 1:         # down
                    a_board[i][j] = ' '
                    a_board[0][j] = '§'


# loop until the user says 'done' or dies
while True:

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'left':
        player_j -= 1  # move left
    elif command == 'right':
        player_j += 1  # move right
    elif command == 'up':
        player_i -= 1  # move up
    elif command == 'down':
        player_i += 1  # move down

    if board[player_i][player_j] == '?':
        print('you\'ve found a weapon!')
        board[player_i][player_j] = ' '  # remove the weapon from the board
        have_weapon = 1

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        if have_weapon == 1:
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you were caught without a weapon and were slain')
            break

    # Move enemies in random directions
    enemy_move(board)

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy!')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hesitated and were slain!')

                  # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()
