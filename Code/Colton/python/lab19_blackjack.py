
cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 10, 'k': 10, 'q': 10, 'a': 1}
hand_1 = input("What is your first card?\nex.2, 3, J, A\n:").lower()
while hand_1 not in cards.keys():
    hand_1 = input("What is your first card?\nex.2, 3, J, A\n:").lower()
hand_2 = input("What is your second card?\nex.2, 3, J, A\n:").lower()
while hand_2 not in cards.keys():
    hand_2 = input("What is your second card?\nex.2, 3, J, A\n:").lower()
hand_3 = input("What is your third card?\nex.2, 3, J, A\n:").lower()
while hand_3 not in cards.keys():
    hand_3 = input("What is your third card?\nex.2, 3, J, A\n:").lower()


hand_1 = cards[hand_1]
hand_2 = cards[hand_2]
hand_3 = cards[hand_3]

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


