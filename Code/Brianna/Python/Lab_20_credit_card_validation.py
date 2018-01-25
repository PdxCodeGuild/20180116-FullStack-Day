'''

Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints  -DONE
Slice off the last digit. That is the check digit. DONE
Reverse the digits. DONE
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
'''

original_card_number = input("Please enter your 16 digit credit card number to check if it is valid.\n:")

original_card_number = list(original_card_number)
number_list = [int(original_card_number[i]) for i in range(16)]
modified_card_number = original_card_number.copy()

check_number = modified_card_number.pop()

print(check_number)
print(original_card_number)
print(modified_card_number)

reversed_number = modified_card_number[::-1]

print(reversed_number)

doubled_numbers = [int(reversed_number[i]) * 2 if i % 2 == 0 else int(reversed_number[i]) for i in range(len(reversed_number))]
minus_nine = [int(doubled_numbers[i]) -9 if int(doubled_numbers[i]) > 9 else int(doubled_numbers[i]) for i in range(len(doubled_numbers))]

print(doubled_numbers)
print(minus_nine)

#Need to replace minus_nines in doubled_numbers then replace doubled numbers in reversed_numbers