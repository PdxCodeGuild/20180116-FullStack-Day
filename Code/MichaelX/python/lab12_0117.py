import random

guesses = 0
correct = 0

while guesses < 10:

    guess = input('> guess the number?\n> ')

    guesses += 1

    x = random.randint(1, 10)

    if int(guess) == x:
        correct =+ 1
        print('correct')

    elif int(guess) != x:
        print('try again!')


print(f'you got correct {correct} times')