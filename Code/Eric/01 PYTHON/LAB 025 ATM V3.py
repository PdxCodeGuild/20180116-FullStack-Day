class ATM:
	def __init__(self, acct_balance):
		self.acct_balance = acct_balance
		self.interest = ((0.1 / 100) * self.acct_balance)
		self.history = []

	def check_balance(self):
		return print(f'\ncurrent account balance: ${self.acct_balance}')

	def deposit(self):
		deposit_amount = float(input('\nenter deposit amount\n:'))
		self.acct_balance += deposit_amount
		deposit_record = {'time': '', 'transaction type': 'deposit', 'transaction amount': deposit_amount}
		self.history.append(deposit_record)
		return print(f'\ndeposit amount: ${deposit_amount}\nnew account balance: ${self.acct_balance}\n')

	def withdraw(self):
		withdrawal_amount = float(input('\nenter withdrawal amount\n:'))
		if withdrawal_amount > self.acct_balance:
			print(f'sorry! insufficient funds\ncurrent balance: {self.acct_balance}\n')
			return atm.main_menu()
		else:
			self.acct_balance -= withdrawal_amount
			withdraw_record = {'time': '', 'transaction type': 'withdrawal', 'transaction amount': withdrawal_amount}
			self.history.append(withdraw_record)
			return print(f'\nwithdrawn: ${withdrawal_amount}\nnew account balance: ${self.acct_balance}\n')

	def trans_history(self):
			for transaction in self.history:
				print(transaction)

	def interesting(self):
		balance_w_interest = (self.acct_balance + self.interest)
		return print(f'\ncurrent total interest: ${self.interest}\ncurrent balance with interest: ${balance_w_interest}\n')

	def main_menu(self):
		user_main_menu = ''
		print('\nwelcome to our atm machine!\n')
		while True:
			print('\nmain menu:\n'
			       '01- CHECK BALANCE: ("check"/ "balance")\n'
			       '02- DEPOSIT: ("deposit")\n'
			       '03- WITHDRAW: ("withdraw")\n'
			       '04- TRANSACTION HISTORY: ("history"/ "statement")\n'
			       '05- INTEREST STATUS: ("interest")\n'
			       '06- EXIT/ QUIT: ("exit"/ "quit")\n')
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
