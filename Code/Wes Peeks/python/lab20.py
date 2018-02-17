# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.


def second_digit(user_card):  # getting second digit
    if user_card < 10:
        return user_card
    else:
        return user_card % 10


def last_of_the_digits(credit_card_list):

    for i in range(0, len(credit_card_list)):
        credit_card_list[i] = int(credit_card_list[i])

    last_digit = credit_card_list.pop()
    credit_card_list.reverse()

    for i in range(0, len(credit_card_list), 2):
        credit_card_list[i] *= 2
        if credit_card_list[i] > 9:
            credit_card_list[i] -= 9

    total = sum(credit_card_list)
    return total, last_digit


def checker(get_digit, digit2):
    get_digit = second_digit(get_digit)

    if get_digit == digit2:
        print('valid')
    else:
        print('not valid')


def main():
    # user_card = input("Card number")
    user_card = '4556737586899855'
    credit_card_list = list(user_card)
    total_val, last_digit = last_of_the_digits(credit_card_list)
    checker(total_val, last_digit)


main()
