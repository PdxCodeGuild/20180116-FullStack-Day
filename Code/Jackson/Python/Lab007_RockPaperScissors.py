"""
Rock Paper Scissors Lab
"""

import random

#Get input from the user: rock, paper, scissors

userplay = input('choose one of the following: rock, paper, or scissors: ').lower()

#Make a selection for the computer's play and print

computerplay = random.choice(['rock', 'paper', 'scissors'])
print('I choose: ' + computerplay)

#Tell the user whether they won, lost, or tied

if userplay == 'rock':
    if computerplay == 'rock':
        print("you tied")
    elif computerplay == 'paper':
        print("you lose")
    elif computerplay == 'scissors':
        print("you win")
    else:
        print("please try again")

if userplay == 'scissors':
    if computerplay == 'rock':
        print("you lose")
    elif computerplay == 'paper':
        print("you win")
    elif computerplay == 'scissors':
        print("you tie")
    else:
        print("please try again")

if userplay == 'paper':
    if computerplay == 'rock':
        print("you win")
    elif computerplay == 'paper':
        print("you tie")
    elif computerplay == 'scissors':
        print("you lose")
    else:
        print("please try again")

