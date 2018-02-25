"Version 3: Guess the number"
"Also tells user if guess is too high or low"
import random

#allow user to guess infinite times then tell user if they won or lost
#user is told they won and game exits

x = random.randint(1, 10)

i = 1
while True:
    number_guess = int(input('Guess the number: '))
    if number_guess > x:  # telling user if too high
        print('too high ;)')
    elif number_guess < x:
        print('too low low low')  # telling user if too low
    elif number_guess == x:
        print('Correct! You guessed ' + str(i) + ' times. Farewell :)')
        break
    i += 1
