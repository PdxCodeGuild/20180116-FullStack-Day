"""
Lab 19
More gambling!
"""

import random

card_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_dict = {'A': [1, 11], '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


def deal():
    return random.choice(card_list)


"""
    Less than 17, advise to "Hit"
    Over or equal to 17, advise to "Stay"
    Exactly 21, advise "Blackjack!"
    Over 21, advise "Already Busted"

"""

player_cards = list(input("Enter your first card: "))
player_cards.append(input("Enter your second card: "))
player_cards.append(input("Enter your third card: "))

if 'A' in player_cards:
    total = 0
    player_cards.remove('A')

    for i in range(len(player_cards)):
        total += card_dict[player_cards[i]]

    if total < 12:
        ace_value = card_dict['A'][1]
        total += card_dict['A'][1]
        player_cards.append('A')
        print(f"Ace value: {ace_value}")
    else:
        ace_value = card_dict['A'][0]
        total += card_dict['A'][0]
        player_cards.append('A')
        print(f"Ace value: {ace_value}")

else:
    total = 0
    for i in range(len(player_cards)):
        total += card_dict[player_cards[i]]

print(f"You have: {', '.join(player_cards)}")
print(f"Your current total is: {total}")

if total > 21:
    print("Already busted!")
elif total == 21:
    print("Blackjack!")
elif total >= 17:
    print("Stay")
else:
    print("Hit")

