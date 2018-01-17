# import random

import random

# print introduction to game

print('Lets play Rock-Paper-Scissors!')

# ask user for input

user_response = input('Choose: rock, paper, or scissors: ')

# create list for random choice

computer_options = ['scissors', 'rock', 'paper']

# define computer choice

computer_choice = random.choice(computer_options)

#write if statements for possible outcomes

if computer_choice == user_response:
    print('It\'s a tie!')
if computer_choice == 'rock' and user_response == 'scissors':
    print('The computer chose rock.  You lose')
if computer_choice == 'scissors' and user_response == 'rock':
    print('The computer chose scissors. You win!')
if computer_choice == 'rock' and user_response == 'paper':
    print('The computer chose rock.  You win!')
if computer_choice == 'paper' and user_response == 'rock':
    print('The computer chose paper. You lose')
if computer_choice == 'scissors' and user_response == 'rock':
    print('The computer chose scissors. You Win')
if computer_choice == 'rock' and user_response == 'scissors':
    print('The computer chose rock. You lose')
if computer_choice == 'paper' and user_response == 'scissors':
    print('The computer chose paper. You win')
if computer_choice == 'scissors' and user_response == 'paper':
    print('The computer chose scissors. You lose')
