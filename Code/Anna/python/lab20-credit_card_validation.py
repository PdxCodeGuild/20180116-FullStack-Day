"""
Lab 20
Credit Card Validation
"""

import random

"""
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. 
The steps are as follows:

    Convert the input string into a list of ints
    Slice off the last digit. That is the check digit.
    Reverse the digits.
    Double every other element in the reversed list.
    Subtract nine from numbers over nine.
    Sum all values.
    Take the second digit of that sum.
    If that matches the check digit, the whole card number is valid.

"""

print("Give me your credit card number! I promise I won't buy anything...")
card = input("> ")

    # old way - using loops

    # card = []
    #
    # for i in range(16):
    #     card.append(str(random.randint(1, 10)))

# new way - getting fancy with list comprehension

# card = [str(random.randint(1, 9)) for i in range(16)]

cc = str(''.join(card))

print(cc)
print(card)
# print(type(card[0]))


def cc_validation(cc_number):
    numbers = [int(cc_number[i]) for i in range(16)]        # convert to ints
    # print(numbers)
    # print(type(numbers[0]))
    last_digit = numbers.pop()                              # pop that last digit
    print(last_digit)
    print(numbers)

    # reverse = [numbers.pop() for i in range(15)]          # using list comprehension
    # print(reverse)

    reverse = numbers[::-1]                                 # the better way to do it
    print(reverse)

    double = [reverse[i] * 2 if i % 2 == 0 else reverse[i] for i in range(len(reverse))]
    print(double)

    subtract = [double[i] - 9 if double[i] > 9 else double[i] for i in range(len(double))]
    print(subtract)

    sums = sum(subtract)
    print(sums)

    second_digit = str(sums)[1]
    second_digit = int(second_digit)
    print(second_digit)

    if second_digit == last_digit:
        print("Valid!")
    else:
        print("No shopping for you! :(")


cc_validation(card)
