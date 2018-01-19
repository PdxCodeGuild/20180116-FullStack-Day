#Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost.
#If the user guesses the number, the user is told they've won and the game exits. You can get a random number using random.randint:

import random

rand_num = random.randint(1, 10)
print(rand_num)
player1 = int(input('Pick a number, 1-10.\n:'))
count = 1

while player1 != rand_num and count < 10:
    if player1 > rand_num:
        print('Too high')
    if player1 < rand_num:
        print('Too low')
    count += 1
    player1 = int(input('Guess Again.\n:'))

if player1 == rand_num:
    print('yay')
else:
    print('Limit')

print(str(count) + ' Attempts')


