import random

"rock" > "scissors"
"scissors" > "paper"
"paper" > "rock"

jan_ken_list = ["rock", "paper", "scissors"]
computer_choice = random.choice(jan_ken_list)

go_on = True

while go_on is True:
    user_choice = input("Please choose rock, paper, or scissors?\n:")
    if user_choice == computer_choice:
        print("Tie! Well done!")
    elif user_choice != computer_choice:
        if computer_choice > user_choice:
            print("You lose!")
        elif computer_choice < user_choice:
            print("You win!")

    else:
        print("I don't understand.")
    go_again = input("Would you like to go on? (yes or no?)\n:")
    if go_again == "yes":
        print("okay!")
        go_on = True
    elif go_again == "no":
        print("See you later!")
        go_on = False
    else:
        print("I didn't understand...um...let's play again!")
        go_on = True