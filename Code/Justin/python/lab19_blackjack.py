import random

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

deck = ['2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6',
        '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10',
        'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']


# Initialize player card list and card value list
done = False # Game finishes when player stays or busts
cards = []
values = []


# Get card 1:
cards.append(deck.pop(random.randint(0,len(deck)-1)))
print(f'Card number 1: ', cards[0])
values.append(card_values[cards[0]])


# Get card 2:
cards.append(deck.pop(random.randint(0,len(deck)-1)))
print(f'Card number 2: ', cards[1])
values.append(card_values[cards[1]])


score = sum(values)
print(score)

# Check for Blackjack
if score == 21:
    done = True
    print('Blackjack!!!')

card_number = 2

while not done:

    if score > 21:
        if 11 in values:
            values[values.index(11)] = 1
            score = sum(values)
            print('Ace is 1')
            print(score)
        else:
            done = True
            print('Bust!!!')

    score = sum(values)
    if score == 21:
        done = True
        print ('You got 21')
    elif score >= 17 and score < 21:
        done = True
        print('Stay')
    elif score < 17:
        print('Hit')
        card_number += 1

        # Get player cards, quit if not valid
        card = deck.pop(random.randint(0,len(deck)-1))
        print(f'Card number {card_number}: ', card)
        cards.append(card)
        values.append(card_values[card])

        # print(cards)
        # print(values)
        score = sum(values)
        print(score)
