cards_values = {'1': '1', '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

play = True

while play:

    # Initialize player card list and card sum
    cards = []
    sum = 0

    # Get player cards, quit if not valid
    for i in range(3):
        card = input(f'Enter card {i+1}')
        if card not in cards_values:
            play = False # End play
            break
        cards.append(card)

    # Get sum of cards
    for card in cards:
        print(card)
        sum += cards_values[card]
    print(sum)

    # Special case for at least one Ace
    if sum <= 11 and 'A' in cards:
        sum += 10

    # Print suggestestion
    if sum < 17:
        print (sum, ' Hit')
    elif sum >= 17 and sum < 21:
        print (sum, ' Stay')
    elif sum == 21:
        print(sum, ' Blackjack!')
    else:
        print (sum, ' Busted')
    # Play again unless play = False
