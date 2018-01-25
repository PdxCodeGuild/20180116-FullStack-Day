# Blackjack advisor
# First, ask the user for three playing cards.
# Save the user's inputs as a string: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K.


def get_hand_val(hand):
    ace = False
    u_hand_val = 0
    for card in hand:
        try:
            u_hand_val += int(card)
        except ValueError:
            if card.upper() in ['J', 'Q', 'K']:
                u_hand_val += 10
            elif card.upper() == 'A':
                ace = True  # triggers ace evaluation
                u_hand_val += 1  # set ace to 1 for now
    if ace:  # determination of ace value
        if u_hand_val + 10 <= 21:
            u_hand_val += 10
    return u_hand_val


def advise(hand_value):
    if hand_value < 17:
        print(f'With a hand value of {hand_value}, I\'d advise "Hit"')
    elif hand_value == 21:
        print('That\'s 21! Blackjack!')
    elif 17 < hand_value < 21:
        print(f'Your hand value is {hand_value}. I\'d advise "Stay"')
    else:
        print(f'Your hand value is {hand_value}. You\'ve already busted.')


def play():
    card_list = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    u_cards = []
    print(f'Blackjack advice!\nFirst, enter the cards you have. (Inputs accepted: {card_list})')
    for i in range(3):
        u_cards.append(input(f'Enter card {i+1}: '))
        print(f'Your cards: {", ".join(u_cards)}')
    u_hand_val = get_hand_val(u_cards)
    print(f'\tHand value: {u_hand_val}')
    advise(u_hand_val)


play()
