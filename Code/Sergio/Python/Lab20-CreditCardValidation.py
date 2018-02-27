"Lab 20: Credit Card Validation"

credit_card = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]

#  create check_digit for validation later in the process
#  also removes last number
check_digit = credit_card.pop()

#  reverses credit card nums
credit_card = credit_card[::-1]

#  doubles numbers
for i in range(0, len(credit_card), 2):
    credit_card[i] *= 2

#  Subtract nine from numbers over nine.
for i in range(0, len(credit_card)):
    if credit_card[i] > 9:  # check if a number over 9
        credit_card[i] -= 9  # if it is, subtract 9

#  take second digit of sum, if second digit matches the check digit == True
second_digit = sum(credit_card) % 10

#  final check
if second_digit == check_digit:
    print('Credit card is valid!')
else:
    print('Credit card invalid')


