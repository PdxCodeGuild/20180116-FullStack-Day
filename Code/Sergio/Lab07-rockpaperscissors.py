import random
while True:
    options = ['rock', 'paper', 'scissors']
    end_game = 'stop'
    user_choice = input('Choose rock, paper, or scissors: ')
    computer_choice = random.choice(options)

    if user_choice == 'rock':
        if computer_choice == 'rock':
            print('Tie')
        elif computer_choice == 'paper':
            print('Win')
        elif computer_choice == 'scissors':
            print('Lose')
    if user_choice == 'paper':
        if computer_choice == 'rock':
            print('Tie')
        elif computer_choice == 'paper':
            print('Win')
        elif computer_choice == 'scissors':
            print('Lose')
    if user_choice == 'scissors':
        if computer_choice == 'rock':
            print('Tie')
        elif computer_choice == 'paper':
            print('Win')
        elif computer_choice == 'scissors':
            print('Lose')
    if user_choice == end_game:
        break
