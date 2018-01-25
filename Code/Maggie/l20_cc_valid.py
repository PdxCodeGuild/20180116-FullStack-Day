# Credit card validation


import random


def gen_rand_cc():  # Generate a 16 digit string to validate:
    cc_string = ''
    for i in range(16):
        cc_string += str(random.randint(0, 9))
    return cc_string


def check_valid_cc(numstr):  # Check procedure to validate card
    print(f'1. original card number string: \t\t{numstr}')
    check_num = int(numstr[-1])
    print(f'2. Last digit sliced from number as a check digit: \t\t{check_num}')
    cc_chk = [int(x) for x in ((numstr[14::-1]))]  # reversed list of nums 1-15
    print(f'3. List of card numbers 1-15 reversed: \t{cc_chk}')
    # cc_chk[i] *=2 for i in range(len(cc_chk)) if i % 2 != 0  # attempt as a list comprehension
    for i in range(len(cc_chk)):  # double every other digit in list
        if i % 2 != 0:
            cc_chk[i] *= 2
    print(f'4. Every other number in the list doubled: \t{cc_chk}')
    for i in range(len(cc_chk)):  # subtract 9 from any number > 9
        if cc_chk[i] > 9:
            cc_chk[i] -= 9
    print(f'5. 9 subtracted from every number above 9: \t{cc_chk}')
    cc_chk_sum = sum(cc_chk)
    print(f'6. The sum of the listed numbers: \t\t\t{cc_chk_sum}')
    sum_2nd = cc_chk_sum % 10
    seven = f'7-8. Evaluate whether the second number from the sum ({sum_2nd}) matches the check number ({check_num}):'
    print(seven, sum_2nd == check_num)


card_num = gen_rand_cc()
check_valid_cc(card_num)
