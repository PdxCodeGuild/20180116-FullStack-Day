"""
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.
First, ask the user for three playing cards. Save the user's inputs as a string: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q,
or K.
Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are
worth 10. At this point, assume aces are worth 1.
Now, in Blackjack, aces can be worth 11 if they won't put the total point value of both cards over 21.
Lastly, figure out what the playing advice will be. Use the following rules:
    Less than 17, advise to "Hit"
    Over or equal to 17, advise to "Stay"
    Exactly 21, advise "Blackjack!"
    Over 21, advise "Already Busted"
    Then print out the current total point value and the advice.

"""
sum = 0
outcomes = []
aces = 0

#ask the user for their 3 cards
card1 = input('what is your first card?: ').lower()
card2 = input('what is your second card?: ').lower()
card3 = input('what is your third card?: ').lower()

#give Ace a value of one and then check if you can add 10 to it later and if there was an ace
if card1 == 'a':
   aces += 1

if card2 == 'a':
   aces += 1

if card3 == 'a':
   aces += 1

#create a dictionary to convert with Ace as 1
values = {'a': 1,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 10, 'q': 10, 'k': 10}

#Add up values
sum = values[card1] + values[card2] + values[card3]

#3 aces
if aces == 3:
    print(f'{sum} or 13 hit')


#suggest what user should do
if aces < 3:
    if sum < 17:
        print(f'{sum} Hit')
    elif sum < 21 and sum >= 17:
        print(f'{sum} Stay')
    elif sum == 21:
        print(f'{sum} Blackjack!')
    else:
        print(f'{sum} Already Busted')

#1 or 2 aces
if aces < 3 and aces > 0:
    sum += 10
    print('or')
    if sum < 17:
        print(f'{sum} Hit')
    elif sum < 21 and sum >= 17:
        print(f'{sum} Stay')
    elif sum == 21:
        print(f'{sum} Blackjack!')
    else:
        print(f'{sum} Already Busted')



