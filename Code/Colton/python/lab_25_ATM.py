class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.transactions = []

    def main_menu(self):
        while True:
            user = input("Welcome to the bank of capitalist pigs. Pick an option\n Balance\nCheck withdraw\nDeposit\nWithdraw\nPrint Transactions\n:")
            if user == 'balance':
                ATM.check_balance(self)
            elif user == 'check withdraw' or 'check':
                ATM.check_withdrawal(self)
            elif user == 'deposit':
                ATM.deposit(self)
            elif user == 'withdraw':
                ATM.withdraw(self)
            elif user == 'print transaction' or 'print':
                ATM.print_transactions(self)
            elif user == 'done' or 'quit':
                quit()
            else:
                print("Invalid input. Try again")
                atm.main_menu()

    def check_balance(self):
        return print(f'''Your account balance is {self.balance}''')

    def deposit(self):
        deposit_amount = float(input("How much do you want to deposit?"))
        self.balance += deposit_amount
        self.transactions.append(f'''User deposited ${deposit_amount}.''')
        return print( f'''You deposited ${deposit_amount}. Your new balance is {self.balance}''')


    def check_withdrawal(self):
        check_amount = float(input("How much do you want to withdraw?"))
        if check_amount <= self.balance:
            return print(f'''You may make a withdrawal''')
        else:
            return print(f'''You broke mutha fucka''')

    def withdraw(self):
        withdraw_amount = float(input("How much do you want to withdraw?"))
        if withdraw_amount <= balance:
            self.balance -= amount
            self.balance.append(f'''User withdrew ${withdraw_amount}.''')
            return print(f'''You withdrew ${withdraw_amount}. Your new balance is ${balance}.''')
        else:
            return print(f'''You dont have enough money dummy.''')

    def calc_interest(self):
        self.balance += self.balance * self.interest_rate



    def print_transactions(self):
        return print(f'''Users transactions \n...\n'''.join(self.transactions))






atm = ATM(1000000.00)
atm.main_menu()










