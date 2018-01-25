'''
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.

First, ask the user for three playing cards. Save the user's inputs as a string: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K.

Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1.

Now, in Blackjack, aces can be worth 11 if they won't put the total point value of both cards over 21.

Lastly, figure out what the playing advice will be. Use the following rules:

Less than 17, advise to "Hit"
Over or equal to 17, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Then print out the current total point value and the advice.
'''

hand = []
ask = 0

while ask < 3:
    new_card = input("What is your card?\n:").lower()
    face_cards = ('k', 'q', 'j')
    ace =('a')
    if new_card in face_cards:
        new_card = 10
    elif new_card in ace:
        new_card = 1
    else:
        new_card = int(new_card)
    hand.append(new_card)
    ask = ask + 1

hand_value = sum(hand)

if hand_value < 17:
    print(f'hit. Your hand value is {hand_value}.')
elif hand_value >= 17:
    print(f'Stay. Your hand value is {hand_value}.')
elif hand_value == 21:
    print('Blackjack!!!')
elif hand_value > 21:
    print(f'Already busted! Your hand value was {hand_value}.')
