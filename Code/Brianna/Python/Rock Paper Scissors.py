import random

"rock" > "scissors"
"scissors" > "paper"
"paper" > "rock"

jan_ken_list = ["rock", "paper", "scissors"]
user_choice = input("Please choose rock, paper, or scissors?\n:" )
computer_choice = random.choice(jan_ken_list)

if user_choice == computer_choice:
    print("Tie! Well done!")
elif user_choice != computer_choice:
    if computer_choice > user_choice:
        print("You lose!")
    elif computer_choice < user_choice:
        print("You win!")

else:
    print("I don't understand.")