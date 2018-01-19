# Number to phrase converter
# Current version 0.1, works for numbers up to 999
# Convert a given number into a spelled out string.

import random

testnum = random.randint(0, 999)
print('randomly generated number = ', testnum)

# TODO:  change globals into arguments that are passed into functions, so that a testscript can verify that the function works for lots of numbers
# TODO:  convert a number

ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: ''}
teens = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}
tens = {2: 'twenty', 3: 'thirty', 4:'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

#  globals
get_hundreds = testnum // 100
get_tens = testnum // 10 % 10
get_ones = testnum % 10
roman_str = '' #  roman numeral string


def num_phrase(): # getting all of the digits into words
    hundreds_str = ''
    tens_str = ''
    ones_str = ones[get_ones]
    if get_tens == 1: # if the tens digit is in the teens
        tens_str = teens[get_ones]  #output for tens and ones is teens
        ones_str = ''
    elif get_tens > 1: #if the tens is greater than 1, tens string
        tens_str = tens[get_tens]
        if get_ones > 0:
            tens_str += '-'
    if get_hundreds > 0: #if zero in hundreds digit.. don't say hundred
        hundreds_str = (ones[get_hundreds] + ' hundred')
        if get_tens or get_ones > 0:
            hundreds_str += ' and '
    if testnum == 0:
        num_str = 'zero'
    num_str = hundreds_str + tens_str + ones_str
    print(num_str)

num_phrase()