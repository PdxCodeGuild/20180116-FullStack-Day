# Less than 17, advise to "Hit"
# Over or equal to 17, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"


card_value = {"a": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "k": 10, "q": 10,  "j":
              10}

held_cards = []
print('Please enter the numerical value of your cards.')
card1 = input('What is your first card? ')
held_cards.append(card1)
card2 = input('What is your second card? ')
held_cards.append(card2)
card3 = input('What is your third card? ')
held_cards.append(card3)
value = sum(int(i) for i in held_cards)
print(held_cards)
# print(f"Your current cards are: {held_cards}, current value of {value}")

i = value
while i < 22:

    if i < 17:
        print('I advise to hit. ')
        decide = input('Will you hit or stay? ')
        card4 = input('Enter your new card. ')
        held_cards.append(card4)
        value = sum(int(i) for i in held_cards)
        print(f"Your current cards are: {held_cards}, current value of {value}")
    elif i >= 17:
        print('I advise to stay. ')
        print(f"Your current cards are: {held_cards}, current value of {value}")
    elif i == 21:
        print('Blackjack!')
    elif i > 21:
        print('Already busted.')












