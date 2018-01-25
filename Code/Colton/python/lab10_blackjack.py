#######Black Jack###########
# Ask player for 3 inputs#####
# Find the value of cards#####
# if user 11 or above, ace is worth 1, otherwise worth 11
#if less than 17, advise hit
#if more than 17, advise stay
#if user is 21, advise blackjack
#if user above 21, advise bust
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

hand_1 =

print(hand_1)