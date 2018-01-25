

#Take the second digit of that sum.
#If that matches the check digit, the whole card number is valid.
card_number = (input("Enter your 16 digit card number\n:"))
while len(card_number) != 16:
    card_number = input("Card number needs to be 16 digits.\nEnter your 16 digit card number\n:")
card_number = list(card_number)##########converting to list


card_number = [int(i) for i in card_number]#######converting to integers
check_digit = card_number.pop
card_number = card_number[::-1]########reversing the order of the card number
i = 0
print(card_number)
while i < len(card_number):
    card_number[i] *= 2
    if card_number[i] > 9:
        card_number[i] -= 9
    i += 2
card_number = sum(card_number)
card_number = card_number % 10
if card_number == check_digit:
    print("Valid card")
else:
    print("Not valid")







