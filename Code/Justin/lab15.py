
# Convertr integers 0-9999 to corresponding english phrase
# Does not handle 11 - 19 as a special case, rather renames them to "onety-one","onety-two" etc.


# Number_phrases is a list of lists
number_phrases = [['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
                  ['', 'onety-','twenty-', 'thirty-', 'forty-', 'fifty-', 'sixty-', 'seventy-', 'eighty-',
                'ninety-'],
                  ['', 'one hundred ', 'two hundred ', 'three hundred ', 'four hundred ',
                'five hundred ', 'six hundred ', 'seven hundred ', 'eight hundred ',
                'nine hundred '],
                  ['', 'one thousand ', 'two thousand ', 'three thousand ', 'four thousand ',
                'five thousand ', 'six thousand ', 'seven thousand ', 'eight thousand ',
                'nine thousand ']]



n = input ('enter a number between 0 and 9999')
n = int(n)

digit_list = [] # This will be a list of numeric digits generated from user input
word_list = [] # This will be the list of phrases that correspond to digit value and digit index

# Simple check for 0
if n == 0:
    print('zero')


# Make a list of numeric digits from the user input, this list is built backwards
while n > 0:
    digit_list.append(n % 10)
    n //= 10


# Using index of digit and value of digit find the appropriate phrase
# and append to word_list
for i in range(len(digit_list)):
    word_list.append(number_phrases[i][digit_list[i]])

# Phrase list is build in reverse
# Needs to be reversed, joined to a single string, and printed
word_list.reverse()
print("".join(word_list))

