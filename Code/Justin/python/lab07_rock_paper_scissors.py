import random


def get_choices():
    #Asks user for choice
    #Computer randomly gets rock, paper or scissors
    #Returns tuple of user and computer choices
    rps = ['rock', 'paper', 'scissors']

    while True:
        x = input('choose rock, paper or scissors (or \'q\' to quit): ').lower()
        if x in rps or x == 'q':
            break
    y = random.choice(rps)
    return (x, y)


def compare(x, y):
    #Compare user and computer choices returns result as a string
    tie = 'It\'s a tie.'
    win = 'You win!!!'
    lose = 'You lose :('

    #Run through all possible combinations of RPS
    if x == y:
        result = (tie)
    elif x == 'rock' and y == 'paper':
        result = (lose)
    elif x == 'rock' and y == 'scissors':
        result = (win)
    elif x == 'paper' and y == 'scissors':
        result = (lose)
    elif x == 'paper' and y == 'rock':
        result = (win)
    elif x == 'scissors' and y == 'rock':
        result = (lose)
    elif x == 'scissors' and y == 'paper':
        result = (win)

    return result


while True:
    #User plays computer in Rock, Paper, Scissors
    #Games continue until user enters 'q'

    user, computer = get_choices()
    if user == 'q':
        break
    else:
        print("you: ", user, "\ncomputer: ", computer)
        print(compare(user, computer))


print("Goodbye.")


