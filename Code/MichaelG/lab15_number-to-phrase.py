#Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

#Hint: you can use modules to extract the ones and tens digit.

#x = 67
#tens_digit = x//10
#ones_digit = x%10

#Hint 2: use the digit as an index for a list of strings.

ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']


entry = input('Enter a number between 1 and 99: ')
entry = int(entry)

if entry in ones:
    print(ones[entry])

elif entry//10 == 1:
    print(teens[entry % 10])
elif entry//10 > 1:
    print(tens[(entry//10)-2], ones[entry % 10])

