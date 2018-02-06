
cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 10, 'k': 10, 'q': 10, 'a': 1}

def hand(n):
    hand = input("What is your card?\nex.2, 3, J, A\n:").lower()
    while hand not in cards.keys():
        hand = input("What is your card?\nex.2, 3, J, A\n:").lower()
    return hand

hand_1 = cards[hand(1)]
hand_2 = cards[hand(2)]
hand_3 = cards[hand(3)]

master_hand = (hand_1 + hand_2 + hand_3)
print(master_hand)

if master_hand < 17:
    print("Advise hit")
if master_hand > 17:
    print("Advise stay")
if master_hand == 21:
    print("Blackjack!!!")
if master_hand > 21:
    print("Bust")