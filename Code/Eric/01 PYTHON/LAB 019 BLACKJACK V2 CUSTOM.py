# V2: CUSTOM PLAY! 2 CARD DEAL W HIT/STAY OPTION & REPLAYABILITY!
import random  # self explanatory

cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
         'J': 10, 'Q': 10, 'K': 10}  # dictionary of card faces and corresponding values


def card_dealer():  # main game function
	user_hand = []  # list of cards in users hand
	user_hand_val = []  # corresponding value of cards in users hand
	total_val = 0  # total value of aforementioned cards in users hand
	counter = 0  # turn counter
	while counter < 2:  # first hand is a deal of 2 cards while the turn counter is less than 2
		user_card_num = ''  # place holder for a soon to come user card
		if counter == 0:  # if the turn counter is 0
			user_card_num = 'first'  # user receives their 'first' card
		elif counter == 1:  # or else if the turn counter is 1
			user_card_num = 'second'  # the user receives their 'second' card
		card = random.choice(list(cards.keys()))  # variable 'card' is a random choice from the card dictionary up top
		user_hand.append(card)  # the random choice of cards is then appended to the 'user_hand' [an empty list]
		user_hand_val.append(cards[card])  # the corresponding dictionary 'value' of that choice of cards is then appended
		#  to the 'user_hand_val' [another empty list]
		total_val = sum(user_hand_val)  # the total value of the users hand is the sum of the values of the
		# corresponding cards in the list, 'user_hand'
		print('\nyour ' + user_card_num + ' card is ' + card)  # print the users cards in order
		counter += 1  # a turn is over once the user receives a their card
		# this next part accounts for aces in the users first hand
		if total_val > 21:  # if the total_val of user_hand_val is already over 21 after the first 2 card deals
			cards['A'] = 1  # the value of an Ace in the dictionary of cards will remain as 1
		elif total_val <= 10:  # or, if the total_val of user_hand_val is less than or equal to 10
			cards['A'] = 11  # the value of an Ace in the dictionary of cards will be 11
		elif total_val > 10:  # or, if the total_val of user_hand_val is greater than 10 in any way
			cards['A'] = 1  # the value of an Ace in the dictionary of cards will remain as 1
	print('\nyour hand: ' + str(user_hand))  # once the user has their initial hand, print it
	print('card values: ' + str(user_hand_val))  # and print the corresponding values of the cards
	print('total hand value: ' + str(total_val))  # then print the total value of the users hand
	while 21 >= total_val:  # while the total value of the users hand is greater than or equal to 21
		if total_val >= 17:  # if the total value is greater than or equal to 17
			print('\ni would advise that you stay\n')  # advise that the user stay
			stay = input('will you hit or stay?\ntype "hit" or "stay"\n:').lower()  # ask user what their choice will be
			if stay == 'stay':  # if the user chooses to stay
				print('\nyou have chosen to stay. your score is ' + str(total_val))  # print the users score (total_val)
				break  # and break the loop
			elif stay == 'hit':  # or else if the user chooses to hit
				if total_val <= 21:  # and if their score is less than or equal to 21
					user_card_num = 'next'  # the user will receive their 'next' card
					card = random.choice(list(cards.keys()))  # which will be a random choice from the card dictionary
					user_hand.append(card)  # that will be added to the user_hand
					user_hand_val.append(cards[card])  # and the value will be added to their hand value
					total_val = sum(user_hand_val)  # their total score will be updated
					print('\nyour ' + user_card_num + ' card is ' + card)  # new card info will be printed to the user
					# accounts for aces in this condition (same as above)
					if total_val > 21:
						cards['A'] = 1
					elif total_val <= 10:
						cards['A'] = 11
					elif total_val > 10:
						cards['A'] = 1
					print('\nyour hand: ' + str(user_hand))  # print users new hand
					print('card values: ' + str(user_hand_val))  # print value of users cards
					print('total hand value: ' + str(total_val))  # print users new score
					counter += 1  # add a turn
					if total_val == 21:  # if the users score is 21
						print('\n*****B L A C K J A C K!*****\ncongratulations! you win!\n')  # victory
						break
					elif total_val > 21:  # but if the users score goes over 21
						print('\nSORRY! YOU BUSTED & LOST! =(\n')  # defeat
						break
		elif total_val < 17:  # if users score is less than 17
			print('\ni would advise that you hit\n')   # advise that the user hit
			hit = input('will you hit or stay?\ntype "hit" or "stay"\n:').lower()  # what will user do???
			if hit == 'stay':  # should the user choose to stay...
				print('\nyou have chosen to stay. your score is ' + str(total_val))  # give them their score
				break
			elif hit == 'hit':  # but should they choose to hit....
				if total_val <= 21:  # if their score is less than or equal to 21
					user_card_num = 'next'  # theyll receive their next card (same as above
					card = random.choice(list(cards.keys()))  # random card is chosen
					user_hand.append(card)  # and added to the users hand
					user_hand_val.append(cards[card])  # the value too
					total_val = sum(user_hand_val)  # score changes
					print('\nyour ' + user_card_num + ' card is ' + card)  # user is informed of their card
					# accounts for aces in this condition (redundant but it works dont judge me)
					if total_val > 21:
						cards['A'] = 1
					elif total_val <= 10:
						cards['A'] = 11
					elif total_val > 10:
						cards['A'] = 1
					# new card, value, and score is relayed here same as above
					print('\nyour hand: ' + str(user_hand))
					print('card values: ' + str(user_hand_val))
					print('total hand value: ' + str(total_val))
					counter += 1  # new turn
					if total_val == 21:  # if their score is 21
						print('\n*****B L A C K J A C K!*****\ncongratulations! you win!\n')  # more victory
						break
					elif total_val > 21:  # but if its greater than 21
						print('\nSORRY! YOU BUSTED & LOST! =(\n')  # another L
						break
		elif total_val == 21:  # if the score of their first 2 cards is already 21
			print('\n*****B L A C K J A C K!*****\ncongratulations! you win!\n')  # user already won!
			break
		elif total_val > 21:  # but if their score was already over 21 after 2 cards
			print('\nSORRY! YOU BUSTED & LOST! =(\n')  # they already lost!
			break
	return user_hand, user_hand_val, total_val  # return all the important stuff

# welcome screen/ game start & quit options
begin_ = input('\n*** W E L C O M E   T O   B L A C K J A C K! ***\n type "start" to begin game or "quit" to exit\n:').lower()
if begin_ == 'start':
	card_dealer()
elif begin_ == 'quit':
	print('\nthank you for playing! GOODBYE!\n')
	quit()

while True:  # option to play again or to quit game without exiting program
	again_ = input('\nGAME OVER! would you like to play again???\ntype "yes" or "no"\n:').lower()
	if again_ == 'yes':
		card_dealer()
	elif again_ == 'no':
		break

print('\nthank you for playing! GOODBYE!\n')  # remember to always thank the player
quit()
