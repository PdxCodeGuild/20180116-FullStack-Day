import random

def print_number(number):
    # This function prints a list of integers nicely formatted
    for d in number:
        print(d, end = ' ')
    print()

# Make number
card_number = [random.randint(0,9) for i in range(16)]
print_number(card_number)

# Get check digit
check_digit = card_number[-1]

# Remove check digit
card_number_no_check = card_number[0:15]
print_number(card_number_no_check)

# Reverse card number
card_number_reversed = card_number_no_check[15::-1]
print_number(card_number_reversed)

# Double every other digit
card_number_doubled = [card_number_reversed[i] * 2 if i % 2 == 1 else card_number_reversed[i] \
                       for i in range(len(card_number_reversed))]
print_number(card_number_doubled)

# Subtract 9 from every value > 9
card_number_minus9 = [card_number_doubled[i] - 9 if card_number_doubled[i] > 9 else card_number_doubled[i] \
                      for i in range(len(card_number_doubled))]
print_number(card_number_minus9)


# Get sum of values mod 10
check_value = sum(card_number_minus9) % 10

print(sum(card_number_minus9), ' = Sum')
print(check_digit, ' = Check digit')

# Compare sum of values mod 10 to check digit
if check_value == check_digit:
    print('Valid! Let\'s go shopping!')
else:
    print('Not valid :( :( :(')



