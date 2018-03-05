import random

#Initialize global variables
names = []
chips = []
center = 0


def setup():
    # Gets list of player names
    # Each player starts with 3 chips

    name = ''
    while name != 'done':
        name = input("Enter a player's name: ")
        if name == 'done':
            break
        names.append(name)
        chips.append(3)

def current_state():
    print(chips)
    print('center: ', center)
    print('*' * 50)


def roll_die(c):
    dice = ['L', '*', 'C', '*', 'R', '*']
    # c is current players number of chips
    # This function is only called if the current player has more than 0 chips

    if c >= 3:
        return [random.choice(dice), random.choice(dice), random.choice(dice)]
    elif c == 2:
        return [random.choice(dice), random.choice(dice)]
    else:
        return [random.choice(dice)]


def move_chips(left, right, current):
    # variables left, right, current are indices of left, right, current player
    global center
    for item in current_roll:
        if item == 'L':
            chips[current] -= 1
            chips[left] += 1
        elif item == 'R':
            chips[current] -= 1
            chips[right] += 1
        elif item == 'C':
            chips[current] -= 1
            center += 1
        else:
            continue


def check_winner():
    count = 0
    for i in range(len(chips)):
        if chips[i] != 0:
            count += 1
            winner_index = i

    if count == 1:
        print(f'Player {winner_index} wins!!!')
        return True
    else:
        return False


# Set up current game
setup()
number_of_players = len(names)
winner = False
turn_count = 0

# Print initial state
current_state()

# Start game
while winner == False:
    # ID current player, left player, right player
    current_player = (turn_count % len(names))
    left_player = ((turn_count - 1) % len(names))
    right_player = ((turn_count + 1) % len(names))


    print(f'Player {current_player}, your turn.')
    # print(f'Player {left_player}, is left.')
    # print(f'Player {right_player}, is right.')
    input()

    # Get player current roll if player has chips
    if chips[current_player] > 0:
        current_roll = roll_die(chips[current_player])
        print('You rolled: ', current_roll)

        # Move chips depending on roll by updating chip list
        move_chips(left_player, right_player, current_player)

    else:
        print('PASS')


    # Print current state
    current_state()

    # Check winner
    winner = check_winner()

    # Increment turn count
    turn_count += 1
