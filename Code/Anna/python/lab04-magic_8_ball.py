"""
Lab 4
Fun with the Magic 8 Ball!
"""

import random

print("\nAsk the Magic 8 Ball anything!\nTo finish, type 'done'. Enjoy!\n")

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'You may rely on it', 'As I see it, yes', 'Signs point to yes', 'Reply hazy try again', 'Better not tell you now', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

running = True
question = input("Ask your question here: ")

while running == True:
    if question == 'done':
        running = False
    else:
        answer = random.choice(answers)
        print(answer + "\n")
        if answer in answers[0:6]:
            print("Sweet! ")
        else:
            print("That's a bummer, oh well. ")
        question = input("\nAsk another question: ")
