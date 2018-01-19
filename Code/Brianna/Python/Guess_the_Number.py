import random

guess = False
count = 0

print("See if you can find the number the computer selected!")

computer_number = random.randint(1, 1000)

while guess == False:
    user_guess = input("Guess a number between 1 - 1000. :-)\n:")
    count = count + 1
    try:
        user_guess == int(user_guess)
        if int(user_guess) > computer_number:
            print("Too high!")
        elif int(user_guess) < computer_number:
            print("Too Low!")
        elif int(user_guess) == computer_number:
            print('You got it!')
            break
    except ValueError:
        if user_guess == "done" or user_guess == "exit":
            print("Too bad! Better luck next time!")
            break


print(f"That was fun! You guessed {count} times. Let's play again soon! ")

