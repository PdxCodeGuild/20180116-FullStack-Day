"""
Lab 15
Turning numbers into words
"""

print("Give me a number between 0 and 999:")
number = input("> ")
number = int(number)

singles = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
decs = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
hundreds = {1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred', 5: 'five hundred', 6: 'six hundred', 7: 'seven hundred', 8: 'eight hundred', 9: 'nine hundred'}


def num_to_phrase(number):

    if number == 0:
        ones_phrase = "zero"
        return ones_phrase

    elif number < 10:
        ones_digit = number % 10
        return singles[ones_digit]

    elif number < 100:
        tens_digit = number // 10
        ones_digit = number % 10
        return decs[tens_digit] + '-' + singles[ones_digit]

    elif number < 1000:
        interfy = str(number)
        hundreds_digit = number // 100
        tens_digit = int(interfy[1])
        ones_digit = number % 10
        return hundreds[hundreds_digit] + ' ' + decs[tens_digit] + '-' + singles[ones_digit]

    else:
        phrase = "Sorry, your number is too big for my brain."
        return phrase





print("Your number is: " + num_to_phrase(number))