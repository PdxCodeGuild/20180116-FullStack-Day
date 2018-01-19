import math



digits = [['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
          ['', 'onety-','twenty-', 'thirty-', 'forty-', 'fifty-', 'sixty-', 'seventy-', 'eighty-', 'ninety-'],
          ['', 'one hundred ', 'two hundred ', 'three hundred ', 'four hundred ', 'five hundred ', 'six hundred ', 'seven hundred ', 'eight hundred ', 'nine hundred ']]



n = input ('enter a number between 0 and 999')
n = int(n)

digit_list = []
word_list = []

if n == 0:
    print('zero')

while n > 0:
    print(n)
    digit_list.append(n % 10)
    n = math.floor(n / 10)


print(digit_list)

for i in range(len(digit_list)):
    word_list.append(digits[i][digit_list[i]])

print(word_list)
word_list.reverse()
output = "".join(word_list)
print(output)
