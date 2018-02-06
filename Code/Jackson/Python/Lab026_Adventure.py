"""
Let's build a simple board game that runs on the terminal. We'll represent the board using a list of lists. We'll use
two ints to represent that player's position on the board. Every iteration of the game loop, the user will be prompted
for a command. Start with the code below, and add your own modifications.

Changed the icons to be sea themed
allow the user to go around the world

The goal is to go around the world (there's a check to make sure you made it across one of the

**Need to set a boolean to see if has gone around the world yet.  If so,
"""

import random

width = 10  # the width of the board
height = 10  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append('〜')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4

#around the world track
around_the_world = False  # start at False

# add 4 enemies in random locations
class Set_opponents():
    def __init__(self):
        for i in range(4):
            enemy_i = random.randint(0, height - 1)
            enemy_j = random.randint(0, width - 1)
            board[enemy_i][enemy_j] = '☠'

# loop until the user says 'done' or dies
while True:

    command = input('what direction, captain?!: n/s/e/w')  # get the command from the user
    Set_opponents() # set the food/bad guys on the board
    if command == 'done':
        break  # exit the game
    elif command == 'w':
        player_j -= 1  # move left
        if player_j == -1:
            player_j +=10
            around_the_world = True
            Set_opponents()  # double the number of opponents
    elif command == 'e':
        player_j += 1  # move right
        if player_j == 10:
            player_j -= 10
            around_the_world = True
            Set_opponents()  # resets food after going 'around the world'
    elif command == 'n':
        player_i -= 1  # move up
        if player_i == -1:
            player_i += 10
            around_the_world = True
            Set_opponents()  # resets food after going 'around the world'
    elif command == 's':
        player_i += 1  # move down
        if player_i == 10:
            player_i -= 10
            around_the_world = True
            Set_opponents()  # resets food after going 'around the world'

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '☠ ':
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
                print('⛵', end=' ')
            elif i == 4 and j == 4:
                print('🏝', end ='')
            else:
                print(board[i][j], end='')  # otherwise print the board square
        print()

    if player_i == 4 and player_j == 4 and around_the_world == True:
        print('************You win!*****************')
        break
