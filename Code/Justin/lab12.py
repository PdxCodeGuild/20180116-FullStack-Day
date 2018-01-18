import random

x = random.randint(1,100)

guesses = 1
while True:
    guess = input("Guess a number: ")
    try:
        guess = int(guess)
        if guess == x:
            break
        else:
            if guess < x:
                print('Higher.')
            else:
                print('Lower.')
            guesses += 1
    except ValueError:
        print("Enter an integer please.")


print ("\nGood job!")
print ('It only took you', guesses, "tries.")
