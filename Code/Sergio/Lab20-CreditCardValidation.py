"Lab 20: Credit Card Validation"

credit_card = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
print(credit_card)


#  create check_digit for validation later in the process
#  also removes last number
check_digit = credit_card.pop()
print(check_digit)
print(credit_card)

#  removes last number
# credit_card = credit_card[:len(credit_card)-1]
# print(credit_card)


#  reverses credit card nums
credit_card = credit_card[::-1]
print(credit_card)

#  doubles numbers
for i in range(0, len(credit_card), 2):
    credit_card[i] *= 2
print(credit_card)

#  Subtract nine from numbers over nine.
for i in range(0, len(credit_card)):
    if credit_card[i] > 9: # check if a number over 9
        credit_card[i] -= 9 # if it is, subtract 9
print(credit_card)


#  sum all values, should be 85 with the sample credit card number from the lab
sum(credit_card)
print(sum(credit_card))

#  take second digit of sum, if second digit matches the check digit == True
credit_card_validation = True #  boolean

print(sum(credit_card) % 10)
print(check_digit)

#  final check
if sum(credit_card) % 10 == check_digit:
    print(credit_card_validation)
else:
    print('Credit card invalid')
#  sum = sum[:sum-1]





#  prints and reverses sample credit card number, reverses it, then takes out first number (technically the last). Interesting code but TRASH
#credit_card = ([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5][17::-1][1:])