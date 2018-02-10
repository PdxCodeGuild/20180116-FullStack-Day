import random


class weapon:
    def __init__(self, dp = 1):
        self.dp = damage

    def dagger(self):
        damage = 5

    def sword(self):
        damage = 10

class enemy:
    def __init__(self, enemy, hp = 10):
        self.enemy = enemy
        self.hp = health

    def troll(self):
        health = 10

    def goblin(self):
        health = 20




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
for i in range(2):#spawn weapons
    weapon.dagger = random.randint(0, height - 1)
    weapon.sword = random.randint(0, width - 1)
    board[weapon.dagger][weapon.sword] = '⚔'
# add 4 enemies in random locations
for i in range(4):
    enemy.troll = random.randint(0, height - 1)
    enemy.goblin = random.randint(0, width - 1)
    board[enemy.troll] = '§'
    board[enemy.goblin] = '#'
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

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§' or board[player_i][player_j] == '#':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')
            break

            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()