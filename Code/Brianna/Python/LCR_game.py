import random

#Money pot
center_pot = 0
# Make dice

def roll_dice():
    import random
    die = ''
    dice_dictonary = {1 : 'left', 2 : 'right', 3 : 'center', 4 : 'nothing', 5 : 'nothing', 6 : 'nothing'}
    roll = random.randint(1, 6)
    die = dice_dictonary[roll]
    return die

def play():
    players = player_dictonaries()
    global center_pot = 0
    while user_index in range(len(players % len(players)):
        for i in range(0, 6):
           action = roll_dice()
           if action == 'center':
                center_pot = center_pot + 1
           elif action == 'nothing':
                center_pot = center_pot
           elif action == 'left':
                for i in range(players[i+1][1]):
                    players[i]["chips"] = players[i](["chips"] + 1)
           elif action == 'right':
                for i in range(players[i - 1]["chips"]):
                    players[i]["chips"] = players[i](["chips"] + 1)
            


def player_dictionaries():
    players = []
    player_number = int(input('How many players are playing RCL today?\n:'))
    for player_num in range(player_number):
        new_player = {}
        new_player['name'] = input("What is your name?\n:")
        new_player['chips'] = 3
        players.append(new_player)
    return players, player_number


players = player_dictionaries()
print(players)




# make players an automatically populated index/dictionary then L is "money" is assigned to that index -1, R is
#assigned to that index +1.  Use modulous to wrap the index?

# example_list_of_lists[0][0]

