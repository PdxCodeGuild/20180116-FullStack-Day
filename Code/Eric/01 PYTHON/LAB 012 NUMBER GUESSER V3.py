#RANDOM NUMBER GUESSER V3: HIGHER OR LOWER???
import random

comp_number = random.randint(1, 10)

counter = 0

while True:
    counter = counter + 1
    number_of_guesses = counter
    print("\nI am thinking of a number between 1 and 10...")
    user_guess_1 = int(input("\nCan you guess what that number is???\n\n:"))
    if user_guess_1 == comp_number:
        print("\nExcellent! You have guessed correctly after " + str(number_of_guesses) + " guesses! Thank you for playing!\n")
        break
    if user_guess_1 < comp_number:
        print("\nToo low! Sorry, guess again!\n")
    if user_guess_1 > comp_number:
        print("\nToo high! Sorry, guess again!\n")
