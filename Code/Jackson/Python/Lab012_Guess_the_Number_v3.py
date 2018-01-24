"""
Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.

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
        if y > x:
            print('too high!')
        if y < x:
            print('too low!')