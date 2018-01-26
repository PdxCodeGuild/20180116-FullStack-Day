# V2: CUSTOM PLAY! 2 CARD DEAL W HIT/STAY OPTION & REPLAYABILITY!
import random

cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
         'J': 10, 'Q': 10, 'K': 10}



def card_dealer():  #main game function
	user_hand = []
	user_hand_val = []
	total_val = 0
	counter = 0
	while counter < 2:  #first hand is a deal of 2 cards
		user_card = ''
		if counter == 0:
			user_card = 'first'
		elif counter == 1:
			user_card = 'second'
		card = random.choice(list(cards.keys()))
		user_hand.append(card)
		user_hand_val.append(cards[card])
		total_val = sum(user_hand_val)
		print('\nyour ' + user_card + ' card is ' + card)
		counter += 1
		if total_val > 21:  #accounts for aces in the first hand
			cards['A'] = 1
		elif total_val <= 10:
			cards['A'] = 11
		elif total_val > 10:
			cards['A'] = 1
	print('\nyour hand: ' + str(user_hand))
	print('card values: ' + str(user_hand_val))
	print('total hand value: ' + str(total_val))
	while 21 >= total_val:
		if total_val >= 17:  #advise that you stay(with option to hit)
			print('\ni would advise that you stay\n')
			stay = input('will you hit or stay?\ntype "hit" or "stay"\n:').lower()
			if stay == 'stay':
				print('\nyou have chosen to stay. your score is ' + str(total_val))
				break
			elif stay == 'hit':
				if total_val <= 21:
					user_card = 'next'
					card = random.choice(list(cards.keys()))
					user_hand.append(card)
					user_hand_val.append(cards[card])
					total_val = sum(user_hand_val)
					print('\nyour ' + user_card + ' card is ' + card)
					if total_val > 21:  #accounts for aces in this condition
						cards['A'] = 1
					elif total_val <= 10:
						cards['A'] = 11
					elif total_val > 10:
						cards['A'] = 1
					print('\nyour hand: ' + str(user_hand))
					print('card values: ' + str(user_hand_val))
					print('total hand value: ' + str(total_val))
					counter += 1
					if total_val == 21:
						print('\n*****B L A C K J A C K!*****\ncongratulations! you win!\n')
						break
					elif total_val > 21:
						print('\nSORRY! YOU BUSTED & LOST! =(\n')
						break
		elif total_val < 17:  #advise that you hit(with option to stay)
			print('\ni would advise that you hit\n')
			hit = input('will you hit or stay?\ntype "hit" or "stay"\n:').lower()
			if hit == 'stay':
				print('\nyou have chosen to stay. your score is ' + str(total_val))
				break
			elif hit == 'hit':
				if total_val <= 21:
					user_card = 'next'
					card = random.choice(list(cards.keys()))
					user_hand.append(card)
					user_hand_val.append(cards[card])
					total_val = sum(user_hand_val)
					print('\nyour ' + user_card + ' card is ' + card)
					if total_val > 21:  #accounts for aces in this condition
						cards['A'] = 1
					elif total_val <= 10:
						cards['A'] = 11
					elif total_val > 10:
						cards['A'] = 1
					print('\nyour hand: ' + str(user_hand))
					print('card values: ' + str(user_hand_val))
					print('total hand value: ' + str(total_val))
					counter += 1
					if total_val == 21:
						print('\n*****B L A C K J A C K!*****\ncongratulations! you win!\n')
						break
					elif total_val > 21:
						print('\nSORRY! YOU BUSTED & LOST! =(\n')
						break
		elif total_val == 21:
			print('\n*****B L A C K J A C K!*****\ncongratulations! you win!\n')
			break
		elif total_val > 21:
			print('\nSORRY! YOU BUSTED & LOST! =(\n')
			break
	return user_hand, user_hand_val, total_val


card_dealer()

while True:  #option to play again or to quit game
	again_ = input('\nGAME OVER! would you like to play again???\ntype "yes" or "no"\n:').lower()
	if again_ == 'yes':
		card_dealer()
	elif again_ == 'no':
		break

print('\nthank you for playing! GOODBYE!\n')
quit()

