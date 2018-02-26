first_num = input('What is the first number? ')
second_num = input('what is the second number? ')
sum_total = ''
carry = 0

if len(first_num) >= len(second_num):
    bigger = first_num
    smaller = second_num
else:
    bigger = second_num
    smaller = first_num

for i in range(len(bigger) - len(smaller)):
    smaller = '0' + smaller

#print(smaller)

for i in range(len(bigger) - 1, -1, -1):
    sum_place = int(bigger[i]) + int(smaller[i]) + int(carry)
    digit = sum_place % 10
    carry = sum_place // 10
    sum_total = str(digit) + str(sum_total)
    if i ==0 and carry != 0:
        sum_total = str(carry) + sum_total

print(sum_total)