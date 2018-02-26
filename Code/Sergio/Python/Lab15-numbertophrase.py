"""
Lab 09 Nums to Phrase. Numbers 0-99
"""
import random
#  dictionaries separated by ones, teens, and up to 99
ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: ''}
teens = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen',
         8: 'eighteen', 9: 'nineteen'}
other = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

generated_num = random.randint(0, 99)

#  modulus to extract the ones and tens digit.
hundreds_1 = generated_num // 100
tens_1 = generated_num // 10 % 10
ones_1 = generated_num % 10


#  numbers to phrase
def number_phrase():
    hundreds_dict = ''
    tens_dict = ''
    ones_dict = ones[ones_1]
    if tens_1 == 1:  # if 1's
        tens_dict = teens[ones_1]
        ones_dict = ''

    elif tens_1 > 1:  # if 10's
        tens_dict = other[tens_1]
        if ones_1 > 0:
            tens_dict += '-'  # adds hyphen

    english_number = hundreds_dict + tens_dict + ones_dict
    print(f"{generated_num} = {english_number}")


number_phrase()
