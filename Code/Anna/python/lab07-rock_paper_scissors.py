"""
Lab 7
Let's play paper, scissors, rock!
"""

import random

print("\nHello, human. Let's play paper, scissors, rock!")
print("It's your turn. Enter paper, scissors, or rock: ")

options = ['rock', 'paper', 'scissors']
game_on = True

while game_on is True:
    user_choice = input("> ")
    comp_choice = random.choice(options)
    print(f"The computer chose {comp_choice}.")
    user_choice = user_choice.lower()
    game_on = False

    if user_choice == comp_choice:
        print("It's a tie! Let's try again.")
        game_on = True

    elif user_choice == "rock" and comp_choice == "paper":
        print("You lose!")
        game_on = False

    elif user_choice == "rock" and comp_choice == "scissors":
        print("You win!")
        game_on = False

    elif user_choice == "paper" and comp_choice == "rock":
        print("You win!")
        game_on = False

    elif user_choice == "paper" and comp_choice == "scissors":
        print("You lose!")
        game_on = False

    elif user_choice == "scissors" and comp_choice == "paper":
        print("You win!")
        game_on = False

    elif user_choice == "scissors" and comp_choice == "rock":
        print("You lose!")
        game_on = False

    else:
        print("Something's not right. Try again.")
        game_on = True


