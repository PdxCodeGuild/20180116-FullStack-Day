

def credit_card_validation(card_number_input):
	card_number_list = []

	if len(card_number_input) != 16:  # 16 digit cut off
		return print('is invalid! please retry\n:')

	for i in range(0, len(card_number_input)):  # convert string of ints to list format
		card_number_ = card_number_input[i]
		card_number_list.append(int(card_number_))

	check_digit = card_number_list.pop()  # remove last digit & reverse number
	card_number_list.reverse()

	for i in range(0, len(card_number_list), 2):  # double value of every other element
		card_number_list[i] = card_number_list[i] * 2
	total_val = 0

	for i in range(len(card_number_list)):  # subtract 9 from numbers over 9
		if card_number_list[i] > 9:
			card_number_list[i] = card_number_list[i] - 9
		total_val = total_val + card_number_list[i]  # sum all values

	if check_digit == total_val % 10:   # if second digit of sum matches check digit, card is valid
		return print('is valid!')
	else:
		return print('is invalid! please retry\n:')


card_number_input = input('\n please provide your 16 digit credit card number (without spaces) for verification\n\n:')
print('\nyour card number: ' + str(card_number_input))
credit_card_validation(card_number_input)
