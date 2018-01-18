from random import randint

t = ['rock', 'paper', 'scissors']

computer = t[randint(0, 2)]

player = False

while player == False:

    player = input('Rock, paper or scissors? \n> ')

    if player == computer:
        print('Its a Tie!')

    elif player == 'rock':
        if computer == 'paper':
            print('You lose,', computer, 'covers', player)
        else:
            print('You win,', player, 'smashes', computer)

    elif player == 'paper':
        if computer == 'scissors':
            print('You lose,', computer, 'cuts', player)
        else:
            print('You win,', player, 'covers', computer)

    elif player == 'scissors':
        if computer == 'rock':
            print('You lose,', computer, 'smashes', player)
        else:
            print('You win,', player, 'cuts', computer)

    else:
        print('You must have entered something wrong. Please, try again!')

    player = False
    computer = t[randint(0, 2)]