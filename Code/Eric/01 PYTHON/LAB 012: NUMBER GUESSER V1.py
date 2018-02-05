#RANDOM NUMBER GUESSER V1: 10 GUESSES FOR USER
import random

comp_number = random.randint(1, 10)

counter = 0
while True:
    counter = counter + 1
    print("\nI am thinking of a number between 1 and 10...")
    user_guess_1 = int(input("\nCan you guess what that number is???\n\n:"))
    if user_guess_1 == comp_number:
        print("\nExcellent! You have guessed correctly! Thank you for playing!\n")
        break
    if counter <9 and user_guess_1 != comp_number:
        print("\nSorry, guess again!\n")
    if counter >9 and user_guess_1 != comp_number:
        print("\nYou lose!\n")
        break
