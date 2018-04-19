"""
Lab 19
More gambling!
"""

import random

card_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
ace_count = 0


def deal():
    return random.choice(card_list)


"""
    Less than 17, advise to "Hit"
    Over or equal to 17, advise to "Stay"
    Exactly 21, advise "Blackjack!"
    Over 21, advise "Already Busted"

"""

# human version:
# player_cards = list(input("Enter your first card: "))
# player_cards.append(input("Enter your second card: "))
# player_cards.append(input("Enter your third card: "))

# computer dealer version:


def play(player_cards, ace_count):
    if ace_count == 0:
        total = 0
        for i in range(len(player_cards)):
            total += card_dict[player_cards[i]]

    elif ace_count == 1:
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

    elif ace_count == 2:
        total = 0
        player_cards = list(filter(lambda a: a != 'A', player_cards))

        for i in range(len(player_cards)):
            total += card_dict[player_cards[i]]

        if total < 11:
            ace_value = 12
            total += 12
            player_cards.append('A')
            player_cards.append('A')
            print(f"Ace value: {ace_value}")
        else:
            ace_value = 2
            total += 2
            player_cards.append('A')
            player_cards.append('A')
            print(f"Ace value: {ace_value}")

    elif ace_count == 3:
        total = 0
        player_cards = list(filter(lambda a: a != 'A', player_cards))

        for i in range(len(player_cards)):
            total += card_dict[player_cards[i]]

        if total < 11:
            ace_value = 13
            total += 13
            player_cards.append('A')
            player_cards.append('A')
            player_cards.append('A')
            print(f"Ace value: {ace_value}")
        else:
            ace_value = 3
            total += 3
            player_cards.append('A')
            player_cards.append('A')
            player_cards.append('A')
            print(f"Ace value: {ace_value}")

    elif ace_count == 4:
        total = 0
        player_cards = list(filter(lambda a: a != 'A', player_cards))

        for i in range(len(player_cards)):
            total += card_dict[player_cards[i]]

        if total < 11:
            ace_value = 14
            total += 14
            player_cards.append('A')
            player_cards.append('A')
            player_cards.append('A')
            player_cards.append('A')
            print(f"Ace value: {ace_value}")
        else:
            ace_value = 4
            total += 4
            player_cards.append('A')
            player_cards.append('A')
            player_cards.append('A')
            player_cards.append('A')
            print(f"Ace value: {ace_value}")

    print(f"You have: {', '.join(player_cards)}")
    print(f"Your current total is: {total}")
    return total


def game(ace_count):
    cards = []
    hit = True
    total = 0

    while hit is True:
        new_card = deal()
        print(f"The dealer gives you: {new_card}")
        if new_card == 'A':
            ace_count += 1
        cards.append(new_card)
        total = play(cards, ace_count)

        if total > 21:
            print("Busted!")
            hit = False
            break
        elif total == 21:
            print("Blackjack!")
            hit = False
            break
        elif total >= 17:
            print("Stay")
            hit = False
            break
        else:
            print("Hit")
            hit = True

    return total


game(ace_count)
