# User prompt
choice = input('+ or *?\n> ')
first_num = input('What is the first number?\n> ')
second_num = input('What is the second number?\n> ')


# Loops through the digits of each number starting at the ones and finds records the digit and remainder
def addition(one_num, two_num):
    sum_total = ''
    carry = 0
    # Find bigger number in order to set length of both numbers
    if len(one_num) >= len(two_num):
        longer = one_num
        shorter = two_num
    else:
        longer = two_num
        shorter = one_num

    # Add zeroes to the front of the smaller number until lengths are equal.
    for i in range(len(longer) - len(shorter)):
        shorter = '0' + shorter

    for i in range(len(longer) - 1, -1, -1):
        sum_place = int(longer[i]) + int(shorter[i]) + int(carry)
        digit = sum_place % 10
        carry = sum_place // 10
        sum_total = str(digit) + str(sum_total)
        # Adds extra place if remainder for highest places exists
        if i ==0 and carry != 0:
            sum_total = str(carry) + sum_total
    print(str(one_num) + ' + ' + str(two_num) + ' = ' + str(sum_total))


def multiplication(one_num, two_num):
    total = 0
    other_count = 0

    # Find bigger number in order to set length of both numbers
    if len(one_num) >= len(two_num):
        longer = one_num
        shorter = two_num
    else:
        longer = two_num
        shorter = one_num

    # Add zeroes to the front of the smaller number until lengths are equal.
    for i in range(len(longer) - len(shorter)):
        shorter = '0' + shorter

    for i in range(len(shorter) - 1, -1, -1):
        count = 0
        for j in range(len(longer) - 1, -1, -1):
            big_num = longer[j] + ('0' * count)
            product = int(big_num) * int(shorter[i] + '0' * other_count)
            total += product
            count += 1
        other_count += 1
    print(str(one_num) + ' * ' + str(two_num) + ' = ' + str(total))


if choice == '+':
    addition(first_num, second_num)
elif choice == '*':
    multiplication(first_num, second_num)