# ATM V3


class ATM:  # our machine is in a class of its own
	def __init__(self, acct_balance):  # machine initialize, the only important parameter is the balance duh
		self.acct_balance = acct_balance
		self.interest = ((0.1 / 100) * self.acct_balance)  # we are stingy with our interest
		self.history = []  # this will soon be your bank statement lol

	def check_balance(self):
		return print(f'\ncurrent account balance: ${self.acct_balance}')  # self explanatory: checks & relays ur balance

	def deposit(self):
		deposit_amount = float(input('\nenter deposit amount\n:'))  # assuming ur not broke, this input will be a float
		self.acct_balance += deposit_amount  # the (hopefully large) deposit amount gets added to the account balance
		deposit_record = {'time': '', 'transaction type': 'deposit', 'transaction amount': deposit_amount}  # deposit
		#  record is initialized as a blank dictionary with space for custom values
		self.history.append(deposit_record)  # add the current deposit record to our empty list of transactions
		return print(f'\ndeposit amount: ${deposit_amount}\nnew account balance: ${self.acct_balance}\n')  # self
	# explanatory

	def withdraw(self):
		withdrawal_amount = float(input('\nenter withdrawal amount\n:'))  # assuming ur not too broke, this will be a
		# float
		if withdrawal_amount > self.acct_balance:  # if ur too broke or too ambitious for ur account balance
			return print(f'sorry! insufficient funds\ncurrent balance: {self.acct_balance}\n')  # weve all seen this before =(
		else:  # but if ur not too broke
			self.acct_balance -= withdrawal_amount  # some basic math
			withdraw_record = {'time': '', 'transaction type': 'withdrawal', 'transaction amount': withdrawal_amount}
			# ^makes a record of withdrawal which is another blank dictionary w space for custom values
			self.history.append(withdraw_record)  # well put this in the ur bank statement too ;)
			return print(f'\nwithdrawn: ${withdrawal_amount}\nnew account balance: ${self.acct_balance}\n')  # self
		# explanatory

	def trans_history(self):  # this function just loops through our current transaction history to print them in
		# readable format
			for transaction in self.history:
				print(transaction)

	def interesting(self):  # all this does is add our (usually negligible) interest to ur total balance
		balance_w_interest = (self.acct_balance + self.interest)
		# so if you end up looking at ur current interest...
		return print(f'\ncurrent total interest: ${self.interest}\ncurrent balance with interest: ${balance_w_interest}\n')

	def main_menu(self):  # main menu function
		user_main_menu = ''
		print('\nwelcome to our bourgeois atm machine!\n')  # because basic manners are always important
		# even for machines and the bourgeois
		while True:  # as long as ur using the machine u will see the main menu
			print('\nmain menu:\n'
			       '01- CHECK BALANCE: ("check"/ "balance")\n'
			       '02- DEPOSIT: ("deposit")\n'
			       '03- WITHDRAW: ("withdraw")\n'
			       '04- TRANSACTION HISTORY: ("history"/ "statement")\n'
			       '05- INTEREST STATUS: ("interest")\n'
			       '06- EXIT/ QUIT: ("exit"/ "quit")\n')
			# navigation lets u access menu options by keywords in ""s and then calling the corresponding functions
			# including quitting the program/ exiting the machine
			user_main_menu = input('\nwhat would you like to do?\ntype any of the quoted terms to navigate\n:')
			user_main_menu = user_main_menu.lower()
			if user_main_menu == 'check' or user_main_menu == 'balance':
				atm.check_balance()
			elif user_main_menu == 'deposit':
				atm.deposit()
			elif user_main_menu == 'withdraw':
				atm.withdraw()
			elif user_main_menu == 'history' or user_main_menu == 'statement':
				atm.trans_history()
			elif user_main_menu == 'interest':
				atm.interesting()
			elif user_main_menu == 'exit' or user_main_menu == 'quit':
				quit()


atm = ATM(1000.00)
atm.main_menu()
