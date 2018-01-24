"""
Allow the user to make an unlimited number of guesses using a while True and break. Keep track of how many guesses the
user has made, and tell them at the end.

"""

#x is the computer's guess
import random
i = 0
x = random.randint(1, 10)
while True:
    #print('answer:' + str(x)) #to test
    y = int(input('guess the number: '))
    if x == y:
        i += 1
        print('you win! you guessed ' + str(i) + ' times')
        break
    else:
        i += 1
        print('wrong! you have guessed ' + str(i) + ' times, try again!:' )
