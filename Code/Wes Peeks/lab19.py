def card(value):
    if value == 'A':
        return 1
    elif value == 'J' or value == 'K' or value == 'Q':
        return 10
    return int(value)

def hand():
    card1 = input('Which card first?\n:')

    card2 = input ('Which card is second?\n:')

    card3 = input('What is the last card?\n:')

    total = card(card1) + card(card2) + card(card3)
    if 17 > total < 21:
        print('Stay.')
    elif total < 17:
        print('Hit.')
    elif total == 21:
        print('Black Jack.')
    elif total > 21:
        print('Bust.')
    else:
        print('Play Again.')

hand()