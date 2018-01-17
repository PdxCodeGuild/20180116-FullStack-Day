# Lab 7: Rock Paper Scissors
# Let's play rock-paper-scissors with the computer.

# The computer will ask the user for their choice (rock, paper, scissors)
# The computer will randomly choose rock, paper or scissors
# Determine who won and tell the user
# Let's list all the cases:

# rock vs rock (tie)
# rock vs paper
# rock vs scissors
# paper vs rock
# paper vs paper
# paper vs scissors
# scissors vs rock
# scissors vs paper
# scissors vs scissors


import random

x = ['rock','paper','scissors']
y = input('> pick either rock paper or scissors. ')

if y in x:
    picked = random.choice(x)
    print(y + ' ' + picked)

else:
    print('try again')