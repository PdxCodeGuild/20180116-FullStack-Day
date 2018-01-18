'''Guess the number!'''
import random
from time import sleep

guesses = 0

def setup():
    print("Guess the number")
    print("The computer will pick a random number for you to guess")
    secretnum = random.randrange(100)
    print('Ok. The number has been selected\nnow ty to guess it\ninput a number between 1-100')
    guessnum(secretnum)


def guessnum(secretnum):
    global guesses
    guesses += 1
    guess = int(input('Your guess: '))
    if guess < secretnum:
        print('too low! Guess again!')
        guessnum(secretnum)
    elif guess > secretnum:
        print('too high! Guess again!')
        guessnum(secretnum)
    elif guess == secretnum:
        print('That\'s it! You got it in ' + str(guesses) +'  guesses.\nWould you like to play again? (y/n)')
        again = input('Your choice: ')
        if again.upper() == 'Y':
            setup()
            guesses = 0
        else:
            print('Be seeing you!')

setup()