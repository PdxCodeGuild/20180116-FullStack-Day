import random

hands = ['rock', 'paper', 'scissors']
user_hand = ""

print('\nLets play Rock Paper Scissors!!!')
while user_hand.lower() not in hands:
    user_hand = input('\nCHOOSE YOUR WEAPON:\n Rock, Paper, or Scissors?\n:')
    user_hand = user_hand.lower()
opponent = random.choice(hands)
print('\nYour opponents weapon is ' + opponent + '!')

if opponent == 'rock':
    if user_hand == 'paper':
        print('\nYour Paper > Opponents Rock!\n You have emerged victorious!\n')
    elif user_hand == 'scissors':
        print('\nOpponents Rock > Your Scissors\nYou have tasted defeat!\n')
    elif user_hand == 'rock':
        print('\nYour Rock = Opponents Rock\nDRAW!\n')
if opponent == 'paper':
    if user_hand == 'paper':
        print('\nYour Paper = Opponents Paper!\nDRAW!\n')
    elif user_hand == 'scissors':
        print('\nYour Scissors > Opponents Paper!\nYou have emerged victorious!\n')
    elif user_hand == 'rock':
        print('\nOpponents Paper > Your Rock\nYou have tasted defeat!\n')
if opponent == 'scissors':
    if user_hand == 'paper':
        print('\nOpponents Scissors > Your Paper\nYou have tasted defeat!\n')
    elif user_hand == 'scissors':
        print('\nYour Scissors = Opponents Scissors!\nDRAW!\n')
    elif user_hand == 'rock':
        print('\nYour Rock > Opponents Scissors!\nYou have emerged victorious!\n')
