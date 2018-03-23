from random import randint

# Setting game options
throw_item =['Rock', 'Paper', 'Scissors']

#assign a random throw to computer player
computer = throw_item[randint(0,2)]

#Setting player start
player = False

while player == False:
    #conditions for true
    player = input('Rock, Paper, or Scissors?')
    if player == computer:
        print("Tie")
    elif player == 'Rock':
        if computer == 'Paper':
            print('You lose', computer, 'covers', player)
        else:
            print("You win!", player, 'crushes', computer)
    elif player == 'Paper':
        if computer == 'Scissors':
            print('You lose', computer, 'cuts', player)
        else:
            print('You win', player, 'covers', computer)
    elif player == 'Scissors':
        if computer == 'Rock':
            print('You lose', computer, 'breaks', player)
        else:
            print('You win', player,'cuts', computer)
    else:
        print('That\'s not a throw. Please pick one.')
        #setting up the False for player to continue game
    player = False
    computer = throw_item[randint(0,2)]