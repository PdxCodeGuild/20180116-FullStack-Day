"""
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
Version 2: Handle numbers from 100-999.
"""

#ask user for the number
number = int(input('select a number between 1 and 999 and I will convert it to words: '))

#calculate each digit
hundreds_digit = number // 100

tens_digit = (number - (hundreds_digit*100)) // 10

ones_digit = (number - (hundreds_digit*100)) % 10

#checks
#print(hundreds_digit)
#print(tens_digit)
#print(ones_digit)

hundreds_key = {0: '', 1:'one-hundred', 2: 'two-hundred', 3:'three-hundred', 4:'four-hundred', 5: 'five-hundred', \
                6: 'six-hundred', 7: 'seven-hundred', 8: 'eight-hundred', 9:'nine-hundred'}
hundreds_ouput = hundreds_key[hundreds_digit]

if tens_digit == 1:
    teens_key = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', \
                 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}
    tens_output = teens_key[ones_digit]

else:
    tens_key = {0: '', 1:'onety-', 2: 'twenty', 3:'thirty', 4:'forty', 5: 'fifty', \
                6: 'sixty', 7: 'seventy', 8: 'eighty', 9:'ninety'}
    tens_output = tens_key[tens_digit]



ones_key = {0: '', 1:'one', 2: 'two', 3:'three', 4:'four', 5: 'five', \
                6: 'six', 7: 'seven', 8: 'eight', 9:'nine'}
ones_output = ones_key[ones_digit]

print(hundreds_ouput + ' ' + tens_output + ' ' + ones_output)
