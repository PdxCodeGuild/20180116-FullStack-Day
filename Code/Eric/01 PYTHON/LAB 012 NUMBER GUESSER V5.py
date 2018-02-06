#NUMBER GUESSER V5: NOW THE COMPUTER CAN PLAY TOO!
import random

user_number = int(input("Choose a number between 1 and 10. I will try and guess the number.\n\n:"))

counter = 0
previous_guess = ""

while True:
    counter = counter + 1
    number_of_guesses = counter
    comp_guess_1 = random.randint(1, 10)
    print("\n\n:" + str(comp_guess_1))
    if comp_guess_1 == user_number:
        print("\nComputer has guessed correctly after " + str(number_of_guesses) + " guesses! Thank you for playing with me!\n")
        break
    if counter > 1:
        if abs(comp_guess_1) == abs(previous_guess):
            print("\nComputer has guessed the same number as the last =(\n")
        else:
            if abs(comp_guess_1 - user_number) > abs(previous_guess - user_number):
                print("\nI think my last guess was closer...\n")
            elif abs(comp_guess_1 - user_number) < abs(previous_guess - user_number):
                print("\nThis guess was closer than my last...\n")
            else:
                print("\nThat guess was as close as my last!\n")
    if comp_guess_1 < user_number:
        print("Too low! =(\n")
    if comp_guess_1 > user_number:
        print("Too high! =(\n")

    previous_guess = comp_guess_1
