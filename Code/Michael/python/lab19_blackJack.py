import random

cards = {'A': 1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

drawn = {}

for key in cards:
    name, value = random.choice(list(cards.items()))
    drawn[name] = value
    print(name, value)

print(drawn)

# first = input('What\'s your first card?')
# second = input('What\'s your second card?')
# third = input('What\'s your third card?')
#
# h_first = input('What\'s your first card?')
# h_second = input('What\'s your second card?')
# h_third = input('What\'s your third card?')
#
# s_first = input('What\'s your first card?')
# s_second = input('What\'s your second card?')
# s_third = input('What\'s your third card?')
#
# if < 17:
#     print('hit')
#
# elif >= 17:
#     print('stay')
#
# elif == 21:
#     print('blackjack')
#
# elif > 21:
#     print('already busted')
