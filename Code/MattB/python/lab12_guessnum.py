import random

#Computer chooses a random number
num = random.randint(1, 10)

#User imput for first guess
guess = input('Guess a number between 1 and 10: ')

# Number of guesses
ng = 1

while True:
    if ng == 10:
        print('Sorry! You\'re number of guesses is up.')
        break
    elif str(guess) == str(num):
        print(f'Congrats! you guessed {ng} times')
        break
    elif int(guess) < int(num):
        guess = input('Sorry! You\'re guess is too low. Try again: ')
        ng += 1
    elif int(guess) > int(num):
        guess = input('Sorry! You\'re guess is too high. Try again: ')
        ng += 1