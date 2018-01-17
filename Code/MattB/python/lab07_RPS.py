import random

# User prompt for their choice
print('Let\'s play rock, paper, scissors.')
player = input('Choose rock, paper, or scissors: ')

# List for computer's choice
computer = ['rock', 'paper', 'scissors']

c_pick = random.choice(computer)

if c_pick == player:
    print('Tie')
elif c_pick == computer[0] and player == computer[1]:
    print(f'{player} beats {c_pick}. Player wins.')
elif c_pick == computer[0] and player == computer[2]:
    print(f'{c_pick} beats {player}. Computer wins.')
elif c_pick == computer[1] and player == computer[0]:
    print(f'{c_pick} beats {player}. Computer wins.')
elif c_pick == computer[1] and player == computer[2]:
    print(f'{player} beats {c_pick}. Player wins')
elif c_pick == computer[2] and player == computer[1]:
    print(f'{player} beats {c_pick}. Player wins.')
else:
    print(f'{c_pick} beats {player}. Computer wins.')