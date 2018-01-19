# Guess the number!
# This is a game where you try to guess the computer generated number.

import random
import time
import sys
import textwrap

guesses = 0


# cool typing feature
def typer(text, delay=0.03):
    width = 75  # typer is using to determine when to wrap
    for char in textwrap.fill(text, width):
        delay *= random.uniform(0.9, 1.1)
        time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write('\n')


# text and random number, calls guessing function
def setup():
    typer("The computer will pick a random number for you to guess.")
    typer(". . . . . . . . . . . . .")
    secretnum = random.randrange(100)
    time.sleep(.5)
    typer('Ok. The number has been selected\n')
    typer('now try to guess it')
    typer('input a number between 1-100')
    guessnum(secretnum)


# number guessing flow
def guessnum(secretnum):
    while True:
        global guesses
        guesses += 1
        guess = input('Your guess: ')
        try:
            guess = int(guess)
            break
        except ValueError:
            print('Invalid entry! Try again.')
    if guess < secretnum:
        typer('too low! Guess again!')
        guessnum(secretnum)
    elif guess > secretnum:
        typer('too high! Guess again!')
        guessnum(secretnum)
    elif guess == secretnum:
        print('That\'s it! ')
        typer('You got it in ' + str(guesses) + '  guesses.')
        typer('Would you like to play again? (y/n)')
        again = input('Your choice: ')
        if again.upper() == 'Y':
            setup()
            guesses = 0
        else:
            typer('Be seeing you!')


typer("Guess the number")
setup()
