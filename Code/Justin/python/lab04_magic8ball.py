import random

answers = ['Without a doubt', 'As I see it, yes', 'Signs point to yes', 'Ask again later', "Don't count on it"]

while True:
    question = input("What would you like to know? ")
    if question == 'done':
        break
    print(random.choice(answers))