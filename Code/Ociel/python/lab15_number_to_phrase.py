# Version 1

number = int(input('what number do you want to convert into words: '))

zero_to_ten = {0: 'Zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
               6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}

eleven_to_nineteen = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                      16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

twenty_to_ninty = {20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty',
                   60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

hundred = ['hundred']

if number >= 20 and number < 100:
    x = 10 * (number // 10)
    i = number % 10

    if i == 0:
        print(twenty_to_ninty[x])
    else:
        print(twenty_to_ninty[x] + ' ' + zero_to_ten[i])

if 20 > number >= 0:
    if number > 10:
        print(eleven_to_nineteen[number])
    else:
        print(zero_to_ten[number])

#################################################################################
# Version 2 - ADDS THE ONE HUNDREDS

if number >= 120 and number < 1000:
    # x gives my the first number
    # r gives me the remainder of the numbers
    # i also gets the remainder but it subtracts
    # the remainder so tha it can be put into
    # a list to look at the dictionary.
    x = number // 100
    r = number % 10
    i = number % 100 - r
    # if there is zero in r and i then that means it a a complete hundred
    # number so we just at the hundred at the end.

    if r == 0 and i == 0:
        print(zero_to_ten[x] + ' ' + hundred[0])
    elif r == 0 and i != 0:
        print(zero_to_ten[x] + ' ' + hundred[0] + ' and ' +
              twenty_to_ninty[i])
    else:
        print(zero_to_ten[x] + ' ' + hundred[0] + ' and ' +
              twenty_to_ninty[i] + ' ' + zero_to_ten[r])

if number < 120 and number >= 100:
    initial_number = number // 100
    remainder = number % 100

    if number > 110:
        print(zero_to_ten[initial_number] + ' ' + hundred[0] + ' and ' + eleven_to_nineteen[remainder])
    elif remainder > 0:
        print(zero_to_ten[initial_number] + ' ' + hundred[0] + ' and ' + zero_to_ten[remainder])
    else:
        print(zero_to_ten[initial_number] + ' ' + hundred[0])

#################################################################################
# Version 3
