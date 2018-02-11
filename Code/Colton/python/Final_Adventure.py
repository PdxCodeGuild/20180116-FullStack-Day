import random
#Added borders
#Added guessing game to fight goblins
#Added player health
#Sorry, I am not a very creative person

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
for i in range(8):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

# loop until the user says 'done' or dies
while True:

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'left' or command == 'l':
        player_j -= 1  # move left
        if player_j == 0: #######Adding borders
            player_j += 1
    elif command == 'right' or command == 'r':
        if player_j == 9:
            player_j -= 1
        player_j += 1  # move right
    elif command == 'up' or command == 'u':
        if player_i == 0:
            player_i += 1
        player_i -= 1  # move up
    elif command == 'down' or command == 'd':
        if player_i == 9:
            player_i -= 1
        player_i += 1  # move down

    player_health = 20#Adding player health and health is depleted for wrong answers
    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§': #Adding number guesing name for enemies
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            tricky_goblin = random.randint(1, 10)
            print("The enemy wants you to guess a number between 1 and 10 or DIE.")
            while player_health > 0:
                print(f'''PLAYER HEALTH:{player_health}hp''')
                guess = int(input("Guess at your own peril\n:"))
                print(tricky_goblin)

                if guess != tricky_goblin:
                    print("The goblin hit you and did 5 damage")
                    player_health -= 5
                    if player_health <= 0:
                        print("The goblin ate you")
                        quit()

                if guess == tricky_goblin:
                    print("You have slain the tricky goblin")
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