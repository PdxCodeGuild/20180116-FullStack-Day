import time
import random

roll = ['scissors', 'paper', 'rock']

throw = random.choice(roll)

print('Hello')
time.sleep(1.0)
print('Will you choose')
time.sleep(1)
print('Rock')
time.sleep(1)
print('Paper')
time.sleep(1)

scissors2 = input('Or Scissors?')
output = 'You have chosen ' + scissors2
print(output)
print('I choose')
time.sleep(1.5)
print(throw)

if output and throw:
    print('Tie!')
