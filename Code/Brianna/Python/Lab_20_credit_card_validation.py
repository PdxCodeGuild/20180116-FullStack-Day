# Input card number
original_card_number = input("Please enter your 16 digit credit card number to check if it is valid.\n:")

#Make card number into a list
original_card_number = list(original_card_number)
number_list = [int(original_card_number[i]) for i in range(16)]

#Create a modified card number in case I want to print the original etc. at some point.
modified_card_number = original_card_number.copy()

#Get the check number
check_number = modified_card_number.pop()

#Reverse the card number
reversed_number = modified_card_number[::-1]

# Double the numbers
doubled_numbers = [int(reversed_number[i]) * 2 if i % 2 == 0 else int(reversed_number[i]) for i in range(len(reversed_number))]

# Minus nine from numbers greater than nine.
minus_nine = [int(doubled_numbers[i]) -9 if int(doubled_numbers[i]) > 9 else int(doubled_numbers[i]) for i in range(len(doubled_numbers))]

# Sum the card numbers
sum_of_card = sum(minus_nine)

# Make a string to grab number to check
str(sum_of_card)
final_check = str(sum_of_card)[1]

# Check the check number and final check number to see if card is balid. Print outcome.
if int(final_check) == int(check_number):
    print(f"Valid Card! Go and buy something! {check_number} and {final_check} are a match!")
else:
    print(f"This card is not valid. Check numbers {check_number} and {final_check} do not match.")