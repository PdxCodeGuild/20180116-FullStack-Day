#LCR DICE GAME


# Each player receives at least 3 chips. Players take it in turn to roll three six-sided dice

from random import choice

def get_players():  # returns a list of the players in the game
    print('Let\'s play LCR!')
    players = []
    # get a player name, add it to the list, ask for the next player name.
    while True:
        name = input('Enter player name (or "done" when all players entered): ')
        if name.lower() == 'done':
            break
        else:
            players.append(name)
            print(players)
    return players


# give players chips
def setup(players):
    chips = []
    for player in players:
        chips.append(3)
        print(player, 'recieves 3 chips')
    cont = input('press Enter to continue.')
    print('\n')
    return (players, chips)

def play(players, chips):
    pot = 0
    plays = 1
    print('Round', plays)
    die = ['.', '.', '.', 'L', 'C', 'R']
    dice = 3
    while plays < 10:
        for i, player in enumerate(players):
            d_set = []
            print(player, '\'s turn!', player, 'rolls', dice, 'dice.\n')
            for result in range(dice):
                d_set.append(choice(die))
            print('Die results: ', d_set)
            for result in range(len(d_set)):
                if d_set[result] == 'L':
                    print(player, 'passes 1 chip to', players[i - 1])
                    chips[i] -= 1
                elif d_set[result] == 'C':
                    print(player, 'puts a chip in the pot.')
                    chips[i] -= 1
                    pot += 1
                elif d_set[result] == 'R':
                    print(player, 'passes 1 chip to', players[(i + 1) % len(players)])
                    chips[i] -= 1
                    chips[(i + 1) % len(chips)] += 1
            print('\n')
            for player in players:
                print(player, 'currently has', chips[i], 'chips')
            print('pot currently has', pot, 'chips.')
            cont = input('press enter.')
            print('\n')
        plays = + 1
'''
Output should look like this.

Let's let the computer play LCR so we dont have to!
choose the number of players: 3
Each player recieves 3 chips.

Player 1: 3 chips
Player 2: 3 chips
Player 3: 3 chips

Press enter to continue.

Round 1.

With 3 chips remaining, player 1 rolls three dice:
Results: 1: . 2: . 3: L

Player 1 passes 1 chip to Player 3. 
Player 1 now has 2 chips.
Player 3 now has 4 chips.

'''

setup1, setup2 = setup(get_players())
play(setup1, setup2)