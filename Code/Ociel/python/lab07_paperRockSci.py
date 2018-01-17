import random

print("Lets Play Paper, Rock, Scizzors\n")

computerAnswer = random.choice(['p', 'r', 's'])

user = "The User"
machine = "The Machine"
answer = 'yes'

while answer != 'no':
    userAnswer = input("Please type p,r, or s for paper, rock, scizzors respectively: ")

    print("You selected {} and {} selected {}." .format(userAnswer, machine, computerAnswer))
    if userAnswer == computerAnswer:
        print("Its a tie")
    if userAnswer is 'r' and computerAnswer is 'p':
        print('{} wins!'.format(machine))
    if userAnswer is 'r' and computerAnswer is 's':
        print('{} wins!'.format(user))
    if userAnswer is 'p' and computerAnswer is 'r':
        print('{} wins!'.format(user))
    if userAnswer is 'p' and computerAnswer is 's':
        print('{} wins!'.format(machine))
    if userAnswer is 's' and computerAnswer is 'r':
        print('{} wins!'.format(machine))
    if userAnswer is 's' and computerAnswer is 'p':
        print('{} wins!'.format(user))

    answer = input("Would you like to play again (Type Yes or No)")


