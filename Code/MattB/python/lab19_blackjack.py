cards = []

first = input('What\'s your first card? \n> ')
cards.append(first)
second = input('What\'s your second card? \n> ')
cards.append(second)
third = input('What\'s your third card? \n> ')
cards.append(third)


def add(cards):
    value = 0
    for card in range(len(cards)):
        if cards[card] in ['J', 'Q', 'K']:
            value += 10
        elif cards[card] == 'A':
            value += 1
        else:
            value += int(cards[card])
    return value


score = add(cards)

if score < 17:
    print(f'{score} Hit')
elif score < 21:
    print(f'{score} Stay')
elif score == 21:
    print(f'{score} Blackjack!')
else:
    print(f'{score} Already busted!')