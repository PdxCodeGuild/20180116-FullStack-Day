'''
Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess
the number, and the program will tell them whether they're right or wrong.\
'''

#x is the computer's guess
import random
i = 0
while i < 10:
    x = random.randint(1, 10)
    #print('answer:' + str(x)) #to test
    y = int(input('guess the number: '))
    if x == y:
        print('you win! you guessed ' + str(i) + ' times')
        break
    else:
        i += 1
        print('wrong! you have guessed ' + str(i) + ' times, try again!:' )

if i == 10:
    print(' You lose!')





#generate a random number between one and ten
#print(x) #test

#get user input to guess


#tell the user whether they are right or wrong and let them keep playing

