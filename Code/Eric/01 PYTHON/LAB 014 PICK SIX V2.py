import random

game_start1 = input('\nhello! welcome to PICK SIX!\ntype "play" to begin or "stop" to exit!\n\n:')  # game start
game_start1 = game_start1.lower()


# USERS TICKET FUNCTION
def pick6():
	ticket = []
	for num in range(6):  # for each of the 6 number slots in ticket list
		ticket.append(random.randint(1, 99))  # append a random integer between 1 and 99
	return ticket  # return as the users ticket


# WINNING NUMBERS FUNCTION
def winnings(ticket, winners):
	match = 0  # matching numbers start at 0
	for num in range(6):  # for each of the 6 number slots in ticket list
		if ticket[num] == winners[num]:  # if a number on the ticket is identical to a winning number
			match = match + 1  # increase the amount of matching numbers by 1
	payout = [0, 4, 7, 100, 50000, 1000000, 25000000]  # payout values corresponding to the amount of winning numbers
	return payout[match]  # return the users payout


# PLAY GAME FUNCTION
def game():
	winners = pick6()  # run pick6 function for winning numbers
	earned = 0  # earnings start at 0
	spent = 0  # so do expenses
	for g in range(100000):  # for every 100,000 runs of the game
		ticket = pick6()  # run pick6 function for users ticket
		spent = spent + 2  # expenses increase by $2 for every ticket (cost)
		earned = earned + winnings(ticket, winners)  # earnings formula for each winning number on user ticket
	bal = (earned - spent)  # balance calculator
	roi = (bal / spent)  # return on investment calculator

# PRINT USER EARNINGS, LOSSES, BALANCE, & ROI
	print('your total earnings are: $' + str(earned))
	print('your total expenses are: $' + str(spent))
	print('your current balance is: $' + str(bal))
	print('your ROI is: ' + str(roi), '\n\n')


# DOES USER EVEN WANT TO GAMBLE??
if 'play' in game_start1:
	game()
elif 'stop' in game_start1:
	quit()
else:
	game_start2 = input('please type "play" to begin or "stop" to quit\n\n:')
	if 'play' in game_start2:
		game()
	elif 'stop' in game_start2:
		quit()
