"Lab 19: Blackjack Advice"

# Figure out point value of each card individually
# A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K.
card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

# Ask user for their first 3 cards
user_card1 = input('What\'s your first card? ')
user_card2 = input('What\'s your second card? ')
user_card3 = input('What\'s your third card? ')

# Sums up cards
card_sum = 0
card_sum = card_values[user_card1] + card_values[user_card2] + card_values[user_card3]
print(card_sum)

# Card Advice
def play():

    if card_sum < 17:
        print('Hit')
    elif card_sum <= 17:
        print('Stay')
    elif card_sum == 21:
        print('Blackjack!')
    elif card_sum >= 22:
        print('Already busted')

play()
