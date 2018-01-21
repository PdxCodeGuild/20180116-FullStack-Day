#import math

input_number = int(input("Please input a number you would like to convert to it's English equivelent.\n:"))

tens_digit = input_number // 10
ones_digit = input_number % 10
hundreds_digit = input_number // 100
hundred_remainders = input_number % 100

dash = '-'

tens_list = {1: 'ten', 2: 'twenty', 3: 'thirty', 4 :'forty', 5: 'fifty', 6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety'}
singles_list = {0 : 'zero', 1 : 'one',  2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
teens_list = {11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen' }
hundreds_list = {1 : 'one hundred', 2: 'two hundred', 3 : 'three hundred', 4 : 'four hundred', 5 : 'five hundred', 6 : 'six hundred', 7 : 'seven hundred', 8 : 'eight hundred', 9 : 'nine hundred' }


# Check if number is over 100

if input_number >= 100 and input_number:
   hundreds = hundreds_list[hundreds_digit]
   new_tens = hundred_remainders // 10
   new_ones = hundred_remainders % 10
   if hundred_remainders < 20 and hundred_remainders > 10:
      print(f'{hundreds} and {teens_list[hundred_remainders]}')
   elif hundred_remainders < 10:
        print(f'{hundreds} and {singles_list[new_ones]}')
   elif hundred_remainders == 10:
        print(f'{hundreds} and {tens_list[1]}.')
   else:
        print(f'{hundreds} and {tens_list[new_tens] + dash + singles_list[new_ones]}')

elif input_number < 20 and input_number > 10:
    print(teens_list[input_number])
elif input_number < 10:
    print(singles_list[input_number])
elif input_number == 10:
    print(tens_list[1])

else:
    print(tens_list[tens_digit] + dash + singles_list[ones_digit])

