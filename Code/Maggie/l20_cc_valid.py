# Credit card validation

#Generate a 16 digit string to validate:

import random

def gen_rand_cc():
    cc_string = ''
    for i in range(16):
        cc_string += str(random.randint(0,9))
    print(cc_string)

def check_valid_cc(card_num):
    check_num = card_num[-1]
    card_num = card_num[]

cardnum = gen_rand_cc()

