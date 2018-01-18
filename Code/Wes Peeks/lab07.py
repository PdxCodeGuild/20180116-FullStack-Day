import random

choice = ['rock', 'paper', 'scissors']

player = input("Choose: Rock, Paper, or Scissors?\n:")

comp = random.choice(choice)

while player not in choice:
    player = input("Choose: Rock, Paper, or Scissors?\n:")

# Rock
if player == 'rock' and comp == 'rock':
    print(comp + ', Rock Fight! Play again')
elif comp == 'paper':
    print(comp + ', Computer wins!')
elif comp == 'scissors':
    print(comp + ', Sparkly Vampire. Player wins.')
# Paper
elif player == 'paper' and comp == 'rock':
    print(comp + ', Paper Blankey! Player wins.')
elif comp == 'paper':
    print(comp + ', Paper cut. Choose again')
elif comp == 'scissors':
    print(comp + ', Comp wins!')
# Scissors
elif player == 'scissors' and comp == 'rock':
    print(comp + ', Comp wins! Bent Metal.')
elif comp == 'paper':
    print(comp + ', Player wins. Paper confetti.')
elif comp == 'scissors':
    print(comp + ', Scissor fight.')
