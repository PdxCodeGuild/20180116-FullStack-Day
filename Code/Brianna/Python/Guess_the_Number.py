import random

guess = 0

print("See if you can find the number the computer selected!")

computer_number = random.randint(1, 10)

while guess < 10:
    user_guess = int(input("Guess a number between 1 - 10. :-)\n:"))
    if user_guess == computer_number:
        print('You got it!')
        guess = guess + 1
        break
    else:
        print("Too bad! Better luck next time!")
        guess = guess + 1

print("That was fun! Let's play again soon. ")

