# V1: USER INPUTS CARDS
cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
         'J': 10, 'Q': 10, 'K': 10}

def card_dealer():
	user_hand = []
	user_hand_val = []
	total_val = 0
	counter = 0
	while counter < 3:
		user_card = ''
		if counter == 0:
			user_card = 'first'
		elif counter == 1:
			user_card = 'second'
		elif counter == 2:
			user_card = 'third'
		card = input('\nwhat is your ' + user_card + ' card?\n\n:')
		user_hand.append(card)
		user_hand_val.append(cards[card])
		total_val = sum(user_hand_val)
		counter += 1
		if total_val <= 10:
			cards['A'] = 11
		elif total_val > 10:
			cards['A'] = 1
	print('your hand: ' + str(user_hand))
	print('card values: ' + str(user_hand_val))
	print('total hand value: ' + str(total_val))
	if total_val == 21:
		print('\n*****B L A C K J A C K!*****\ncongratulations! you win!\n')
	elif total_val > 21:
		print('\nsorry! you busted & lost! =(\n')
	elif total_val > 17:
		print('\ni would advise that you stay\n')
	elif total_val <= 17:
		print('\ni would advise that you hit\n')
	return user_hand, user_hand_val, total_val


card_dealer()

