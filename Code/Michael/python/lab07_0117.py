# Lab 7: Rock Paper Scissors
# Let's play rock-paper-scissors with the computer.

# The computer will ask the user for their choice (rock, paper, scissors)
# The computer will randomly choose rock, paper or scissors
# Determine who won and tell the user
# Let's list all the cases:

import random

x = ['rock','paper','scissors']
y = input('> pick either rock paper or scissors. ')

win = ['rockscissors', 'rockscissors', 'rockscissors', ]
lose = ['rock vs paper']
tie = ['rock vs paper']


tied = 'rock vs rock'



while y in x:
     computer = random.choice(x)

    if y == computer:

        winner = y + ' vs ' + computer)
    elif y ==


    else:
        print('try again')



# if x and y == rockpaper
#   print(you win, rock covers scissors)

# elif x and y == rockscissors
#   print(you win)