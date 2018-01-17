import random
print('Welcome to the Magic Eight Ball. Press ENTER to play. Type DONE to stop')
while True:
    lottery_list = ['yes', 'no', 'maybe', 'fir sure', 'most def', 'probably not', 'yep', 'you wish', 'nope'] # list of 8 ball options

# Loop infinitely until the user decides to stop "shaking" the magic 8 ball

    shake_ball = input('Shake the magic 8 ball!')

    if shake_ball == '':  # If the user presses enter/return the program will "break" out of the loop??
        print (random.choice(lottery_list))
    else:        # Any other answer will trigger the "else" option
        print ('I hope you enjoyed your future!')
        break
