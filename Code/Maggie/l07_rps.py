'''
Rock, Paper, Scissors

he computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user

After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.
'''

import random
from time import sleep

win = 'You win!!'
lose = 'Computer wins!!'

def start():
    print('Let\'s play a game of rock, paper, scissors!!\nSelect one and challenge the computer.\n')
    abc = input('You can select either "Rock", "Paper", or "Scissors"\na. Rock\nb. Paper\nc. Scissors\n'
               '\nYour choice: ').lower()
    play(abc)

def play(abc):
    index = ''
    options = ['a', 'b', 'c']
    if abc == options[0]:
        print('\nYou chose rock!!')
        index = 0
    elif abc == options[1]:
        print('\nYou chose paper!!')
        index = 1
    elif abc == options[2]:
        print('\nYou chose scissors!!')
        index = 2
    else:
        print('\nPlease make a valid selection\n')
        sleep(1)
        start()
    compare(index)



def again():
    replay = input('Would you like to play again? (Y/N): ').upper()
    if replay == 'Y':
        start()
    else:
        print('Ok. Thank you for playing rock, paper, scissors!')
        sleep(0.5)
        print('goodbye!')

def compare(index):
    choice = random.randrange(2)
    result = (index - choice) % 3
    if choice == 0:
        print('Computer chose rock!!')
    elif choice == 1:
        print('Computer chose paper!!')
    elif choice == 2:
        print('Computer chose scissors!!')
    if result == 1:
        print('You win!!')
    elif result == 0:
        print('You tied!!')
    else:
        print('Computer wins!!')
    print('\n')
    again()

start()
