#RANDOM NUMBER GUESSER V4: HOTTER & COLDER!
import random

comp_number = random.randint(1, 10)

counter = 0
previous_guess = ""

while True:
    counter = counter + 1
    number_of_guesses = counter
    print("\nI am thinking of a number between 1 and 10...")
    user_guess_1 = int(input("\nCan you guess what that number is???\n\n:"))
    if user_guess_1 == comp_number:
        print("\nExcellent! You have guessed correctly after " + str(number_of_guesses) + " guesses! Thank you for playing!\n")
        break
    if counter > 1:
        if abs(user_guess_1) == abs(previous_guess):
            print("\nThat was the same number as your last guess!\n")
        else:
            if abs(user_guess_1 - comp_number) > abs(previous_guess - comp_number):
                print("\nYour last guess was closer...\n")
            elif abs(user_guess_1 - comp_number) < abs(previous_guess - comp_number):
                print("\nThis guess was closer than your last...\n")
            else:
                print("\nThat guess was as close as your last!\n")
    if user_guess_1 < comp_number:
        print("\nToo low! Sorry, guess again!\n")
    if user_guess_1 > comp_number:
        print("\nToo high! Sorry, guess again!\n")

    previous_guess = user_guess_1
