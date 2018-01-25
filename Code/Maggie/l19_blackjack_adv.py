# First, ask the user for three playing cards. Save the user's inputs as a string: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K.


def get_card_val(card):
    try:
        card_val = int(card)
    except ValueError:
        if card.upper() == 'A':
            card_val = 1
        elif card.upper() == 'J' or 'Q' or 'K':
            card_val = 10
    return card_val

def get_hand_val(hand):
    u_hand_val = 0
    for card in hand:
        if card.upper() == 'A':
            hand.remove(card)
            hand.append(card)
    # hand = sorted(hand, reverse=True)
    for card in hand:
        try:
            u_hand_val += int(card)
        except ValueError:
            if card.upper() in ['J', 'Q', 'K']:
                u_hand_val += 10
            elif card.upper() == 'A':
                if u_hand_val + 11 > 21:
                    u_hand_val += 1
                else:
                    u_hand_val += 11
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
    u_hand_val = 0
    print(f'Blackjack advice!\nFirst, enter the cards you have. (Inputs accepted: {(card_list)})')
    for i in range(3):
        u_cards.append(input(f'Enter card {i+1}: '))
        print(f'Your cards: {", ".join(u_cards)}')
    # for card in u_cards:
    #     u_hand_val += get_card_val(card)
    u_hand_val = get_hand_val(u_cards)
    print(f'\tHand value: {u_hand_val}')
    advise(u_hand_val)

play()

