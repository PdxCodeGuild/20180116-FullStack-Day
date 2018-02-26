first_num = input('What is the first number? ')
second_num = input('what is the second number? ')
sum_total = ''
carry = 0

# Find bigger number in order to set length of both numbers
if len(first_num) >= len(second_num):
    bigger = first_num
    smaller = second_num
else:
    bigger = second_num
    smaller = first_num

# Add zeroes to the front of the smaller number until lengths are equal.
for i in range(len(bigger) - len(smaller)):
    smaller = '0' + smaller

# Loops through the digits of each number starting at the ones and finds records the digit and remainder
for i in range(len(bigger) - 1, -1, -1):
    sum_place = int(bigger[i]) + int(smaller[i]) + int(carry)
    digit = sum_place % 10
    carry = sum_place // 10
    sum_total = str(digit) + str(sum_total)
    # Adds extra place if remainder for highest places exists
    if i ==0 and carry != 0:
        sum_total = str(carry) + sum_total

print(sum_total)