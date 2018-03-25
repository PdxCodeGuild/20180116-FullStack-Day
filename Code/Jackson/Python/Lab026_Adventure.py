"""
Let's build a simple board game that runs on the terminal. We'll represent the board using a list of lists. We'll use
two ints to represent that player's position on the board. Every iteration of the game loop, the user will be prompted
for a command. Start with the code below, and add your own modifications.

Changed the icons to be sea themed
allow the user to go around the world
changed the directions to be nautically themed

The goal is to go around the world (there's a check to make sure you made it around the world)
If you encounter a pirate (skull and crossbones) you have to choose a weapon to fight them with.
Cannon beats musket (more power), musket beats sword (more power), sword beats cannon (more agility)
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
        for i in range(5):
            enemy_i = random.randint(0, height - 1)
            enemy_j = random.randint(0, width - 1)
            board[enemy_i][enemy_j] = '/☠'


print('Welcome to "Around the World!"  The objective is to sail around the world and return home without getting capsized by pirates.')

# loop until the user says 'done' or dies
while True:
    command = input('what direction, captain?!: n/s/e/w')  # get the command from the user
    Set_opponents() # set the bad guys on the board each time a mainLoop is made
    if command == 'done':
        break  # exit the game
    elif command == 'w':
        player_j -= 1  # mainLoop left
        if player_j == -1:
            player_j +=10
            around_the_world = True
            Set_opponents()  # double the number of opponents
    elif command == 'e':
        player_j += 1  # mainLoop right
        if player_j == 10:
            player_j -= 10
            around_the_world = True
            Set_opponents()  # resets food after going 'around the world'
    elif command == 'n':
        player_i -= 1  # mainLoop up
        if player_i == -1:
            player_i += 10
            around_the_world = True
            Set_opponents()  # resets food after going 'around the world'
    elif command == 's':
        player_i += 1  # mainLoop down
        if player_i == 10:
            player_i -= 10
            around_the_world = True
            Set_opponents()  # resets food after going 'around the world'

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '/☠':
        print('you\'ve encountered a pirate! You must fight with 1 of the following weapons:"sword, musket, or cannon"')
        computer_play = random.choice(['sword', 'musket', 'cannon'])
        # print(computer_play)  # test to check winning
        user_weapon = input('which weapon do you select?: ').lower()
        print('They choose: ' + computer_play)
        # tie condition
        while computer_play == user_weapon:  # sword > cannon, cannon > musket, musket > sword
            print(f'you both chose {user_weapon}, keep attacking!  What weapon do you choose?: ')
            user_weapon = input('which weapon do you select?: sword, musket, or cannon ')
            computer_play = random.choice(['sword', 'musket', 'cannon'])
            print('They choose: ' + computer_play)
            #losing conditions
        if computer_play == 'sword' and user_weapon == 'cannon':  #tested and worked
            print('sword beats cannon, You Shipwrecked, GAME OVER')
            break
        if computer_play == 'musket' and user_weapon == 'sword':  #tested and worked
            print('musket beats sword, You Shipwrecked, GAME OVER')
            break
        if computer_play == 'cannon' and user_weapon == 'musket':  #tested and worked
            print('cannon beats musket,  You Shipwrecked, GAME OVER')
            break
        # winning conditions
        if user_weapon == 'sword' and computer_play == 'cannon':  # tested and worked
            print('sword beats cannon, you defeated the pirates!')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        if user_weapon == 'musket' and computer_play == 'sword':  # tested and worked
            print('musket beats sword, you defeated the pirates!')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        if user_weapon == 'cannon' and computer_play == 'musket':  # tested and worked
            print('cannon beats musket, you defeated the pirates!')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        # Conditions for unknown weapon
        if user_weapon != 'sword' and user_weapon != 'cannon' and user_weapon != 'musket':
            print(f'{user_weapon} not found on ship.  You shipwrecked, GAME OVER')
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
        print('You returned home safely! \n'
              '************You win!*****************')
        break
