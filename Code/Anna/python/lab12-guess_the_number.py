"""
Lab 12
Let's guess some numbers!
"""

import random

# version 1

print("Welcome to the guessing game! You have 10 guesses.")

computer_guess = random.randint(1, 10)

game_on = True
number_tries = 10

while game_on is True and number_tries > 0:
    user_guess = input("Guess a number between 1 and 10.\n> ")
    user_guess = int(user_guess)
    if user_guess == computer_guess:
        print("You got it in just " + str(10 - number_tries) + " guesses!")
        game_on = False
    else:
        number_tries -= 1
        print("Wrong! You have " + str(number_tries) + " tries left.\n")

print("Game over.\n")

# version 2

print("Let's try another version of the guessing game! This time you have unlimited guesses.")

computer_guess = random.randint(1, 10)

number_tries = 1

while True:
    user_guess = input("Guess a number between 1 and 10.\n> ")
    user_guess = int(user_guess)
    if user_guess == computer_guess:
        print("You got it in just " + str(number_tries) + " guesses!")
        break
    else:
        number_tries += 1
        print("Wrong! Try again.\n")

print("Game over.\n")

# version 3

print("Let's try another version of the guessing game! This time the computer will help you out.")

computer_guess = random.randint(1, 10)

number_tries = 1

while True:
    user_guess = input("Guess a number between 1 and 10.\n> ")
    user_guess = int(user_guess)
    if user_guess == computer_guess:
        print("You got it in just " + str(number_tries) + " guesses!")
        break
    else:
        number_tries += 1
        if user_guess > computer_guess:
            print("Wrong! Too high!\n")
        else:
            print("Wrong! Too low!\n")
print("Game over.")

