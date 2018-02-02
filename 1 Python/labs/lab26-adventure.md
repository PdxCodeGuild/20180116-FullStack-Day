
# Lab 30: Adventure

Let's build a simple board game that runs on the terminal. We'll represent the board using a **list of lists**. We'll use two `int`s to represent that player's position on the board. Every iteration of the game loop, the user will be prompted for a command. Start with the code below, and add your own modifications.

Possible modifications:
- use more succinct commands (l/u/d/r for up/down/left/right or n/s/e/w for north/south/east/west)
- add boundaries to the map, when the player attempts to move beyond the boundary, stop them or move them to the other side
- make what's printed on the screen a part of a much larger map (with the player always shown at the center of the screen)
- loading a text file containing the map, or procedurally generate things
- walls / barriers
- use different unicode characters (you can find [lists online](https://www.google.com/search?q=cool+unicode+characters&rlz=1C1CHBF_enUS773US773&oq=cool+unicode+chara&aqs=chrome.0.0j69i57j0l3.90708j1j1&sourceid=chrome&ie=UTF-8))
- ascii art
- [colorama](https://pypi.python.org/pypi/colorama) for custom colors, or [curses](https://docs.python.org/3/howto/curses.html) for even more control of the terminal
- add 'fog of war' - only show the elements of board immediately around the player (you can then find a torch item, which expands your visibility)
- have enemies move around
- add an inventory system
- add player health, more complex encounters
- add hidden treasure, make the objective to find all the treasure
- add a 'final boss' that you can only face once collecting items
- re-use previous labs (guess the number, rock-paper-scissors)


```python
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

# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

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
    if board[player_i][player_j] == '§':
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

```