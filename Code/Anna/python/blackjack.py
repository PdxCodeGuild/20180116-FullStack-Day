"""
Blackjack Simulator
"""

import random
from time import sleep

card_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


def deal():
    return random.choice(card_list)


"""
    Less than 17, advise to "Hit"
    Over or equal to 17, advise to "Stay"
    Exactly 21, advise "Blackjack!"
    Over 21, advise "Already Busted"

"""


def play(player_cards):
    if 'A' in player_cards:
        total = 0
        player_cards.remove('A')

        for i in range(len(player_cards)):
            total += card_dict[player_cards[i]]

        if total < 12:
            ace_value = 11
            total += 11
            player_cards.append('A')
            print(f"Ace value: {ace_value}")
        else:
            ace_value = 1
            total += 1
            player_cards.append('A')
            print(f"Ace value: {ace_value}")

    else:
        total = 0
        for i in range(len(player_cards)):
            total += card_dict[player_cards[i]]

    print(f"The cards drawn are: {', '.join(player_cards)}")
    print(f"The current total is: {total}")
    return total


def game():
    cards = []
    hit = True
    total = 0

    while hit is True:
        new_card = deal()
        print(f"The space card dealer gives you: {new_card}")
        print('\n'.join(ascii_card(new_card)))
        sleep(2)
        cards.append(new_card)
        total = play(cards)
        choice = input("Do you 'hit' or 'stay'? ")

        if total > 21:
            print("Busted! 😞")
            sleep(2)
            hit = False
            break
        elif total == 21:
            print("Blackjack!")
            print('\n'.join(ascii_card('A')))
            sleep(2)
            hit = False
            break
        elif choice == 'stay':
            print("Stay")
            sleep(2)
            hit = False
            break
        elif choice == 'hit':
            print("Hit")
            sleep(2)
            hit = True
        else:
            print("Not a valid choice")

    return total


def comp_game():
    cards = []
    hit = True
    total = 0

    while hit is True:
        new_card = deal()
        print(f"The ruler gets: {new_card}")
        print('\n'.join(ascii_card(new_card)))
        sleep(2)
        cards.append(new_card)
        total = play(cards)

        if total > 21:
            print("Busted! 😞")
            sleep(2)
            hit = False
            break
        elif total == 21:
            print("Blackjack!")
            print('\n'.join(ascii_card('A')))
            sleep(2)
            hit = False
            break
        elif total >= 17:
            print("Stay")
            sleep(2)
            hit = False
            break
        else:
            print("Hit")
            sleep(2)
            hit = True

    return total


def ascii_card(card):
    # we will use this to prints the appropriate icons for each card
    suits_symbols = ['♠', '♦', '♥', '♣']

    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]

    # "King" should be "K" and "10" should still be "10"
    if card == '10':  # ten is the only one who's rank is 2 char long
        rank = 10
        space = ''  # if we write "10" on the card that line will be 1 char to long
    else:
        rank = card  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
        space = ' '  # no "10", we use a blank space to will the void
    # get the cards suit in two steps
    suit = random.choice(suits_symbols)

    # add the individual card on a line by line basis
    lines[0].append('┌─────────┐')
    lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
    lines[2].append('│         │')
    lines[3].append('│         │')
    lines[4].append('│    {}    │'.format(suit))
    lines[5].append('│         │')
    lines[6].append('│         │')
    lines[7].append('│       {}{}│'.format(space, rank))
    lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    return result
