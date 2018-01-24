# LCR DICE GAME


# Each player receives at least 3 chips. Players take it in turn to roll three six-sided dice

from random import choice


def get_players():  # returns a list of the players in the game
    print('Let\'s have the computer play LCR so that we don\'t have to!')
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
    input('press Enter to continue.')
    print('\n')
    return players, chips


def play(players, chips):
    die = ['.', '.', '.', 'L', 'C', 'R']
    dice = []
    games = 1
    for _ in players:
        dice.append(3)
    while True:
        print('<<GAME', games, '>>')
        # input('\npress enter.\n')
        pot = 0
        plays = 1
        while sum(item > 0 for item in chips) > 1:  # play until 1 player remains
            print('<ROUND', plays, '>')
            for k, player in enumerate(players):
                print(player, 'currently has', chips[k], 'chips')
            input('\npress enter.\n')
            for i, player in enumerate(players):
                if chips[i] == 0:
                    print(player, ' has no chips and passes this turn.')
                    continue
                elif 0 < chips[i] < 3:
                    dice[i] = chips[i]
                else:
                    dice[i] = 3
                d_set = []
                print(player, '\'s turn!', player, 'rolls', dice[i], 'dice.\n')
                for result in range(dice[i]):
                    d_set.append(choice(die))
                print('Die results: ', d_set, '\n')
                for result in range(len(d_set)):
                    if d_set[result] == 'L':
                        print(player, 'passes 1 chip to', players[i - 1], 'on the left.')
                        chips[i] -= 1
                        chips[i - 1] += 1
                    elif d_set[result] == 'C':
                        print(player, 'puts a chip in the pot.')
                        chips[i] -= 1
                        pot += 1
                    elif d_set[result] == 'R':
                        print(player, 'passes 1 chip to', players[(i + 1) % len(players)], ' on the right.')
                        chips[i] -= 1
                        chips[(i + 1) % len(chips)] += 1
                for k, player in enumerate(players):
                    print(player, 'currently has', chips[k], 'chips')
                print('pot currently has', pot, 'chips.')
                input('\npress enter.')
            r_end = input(('end of round', plays, 'press enter to continue or q to quit'))
            if r_end.lower() == 'q':
                break
            plays += 1
        chips[chips.index(max(chips))] = pot  # winner index
        winner = players[chips.index(max(chips))]  # matches chip winner index to name
        print(winner, ' wins this game and takes the pot of', pot, 'chips.')
        for k, player in enumerate(players):
            print(player, 'currently has', chips[k], 'chips')
        # input('\npress enter to continue.')
        print('would you like to play again? ')
        # player chooses to play again. If y, winner score goes into setup with same players
        again = input('"y" to continue or "n" to quit: ')
        if again.lower() == 'y':
            for i in range(len(chips)):
                if chips[i] < 4:
                    chips[i] = 3
            games += 1
            print('OK! Here we go!\n')
            continue
        else:
            print('Ok. Terminating program. Goodbye.')
            break


setup1, setup2 = setup(get_players())
play(setup1, setup2)
