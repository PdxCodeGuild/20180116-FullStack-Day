# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.


# second_digit = get_second_digit(total)  # step 6
# return second_digit == check_digit


# credit_card_str = input('enter your credit card: ')
# credit_card_str = '4556737586899855'
# print(validate_credit_card(credit_card_str))


# user input to list

def your_input(user_card):
    user_card = input('Enter card number.\n:')
    if user_card != 16:
        return False


def second_digit(user_card):  # getting second digit
    if user_card < 10:
        return None
    else:
        return user_card % 10


user_card = input("Card number")


def user_input(user_card):
    credit_card_list = []
    credit_card_list += list(user_card)
    print(credit_card_list)


credit_card_list = list(user_card)
last_digit = ''


def last_of_the_digits(credit_card_list):
    user_input(user_card)
    last_digit = ''
    last_digit += credit_card_list.pop(-1)
    print(last_digit)
    last_of_the_digits(credit_card_list)
    credit_card_list.reverse()
    for i in range(0, len(credit_card_list), 2):
        credit_card_list *= 2
    total = 0

    for i in range(len(credit_card_list)):
        credit_card_list = int(credit_card_list)
    if credit_card_list > 9:
        credit_card_list -= 9

    total += credit_card_list

def checker(get_digit, second_digit):
    get_digit += second_digit(total)

    if get_digit == last_digit:
        print('valid')
    else:
        print('not valid')
