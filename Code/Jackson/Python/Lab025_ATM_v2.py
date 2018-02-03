"""
Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list
saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing
out the list of transactions.
"""

class ATM:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def get_balance(self):
        """ check_balance() returns the account balance """
        return self.balance

    def deposit(self, transaction_amount):  # do I need to use amount, or can this be anything?
        """ deposit(amount) deposits the given amount in the account """
        self.balance += transaction_amount


    def check_withdraw(self, transaction_amount):
        """ check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative """
        if self.balance() - transaction_amount > 0:
            return True

    def withdraw(self, transaction_amount):
        """ withdraw(amount) withdraws the amount from the account and returns it """
        if self.withdrawal(transaction_amount):
            self.balance -= transaction_amount
            self.transactions.append(transaction_receipt)
        return transaction_amount

    def calc_interest(self, transaction_amount, interest_rate):
        """ calc_interest() returns the amount of interest calculated on the account """
        interest_calculated = self.interest_rate * self.transaction_amount

        return self.interest_calculated


    # function that prints out the list of transactions
    def print_transactions(self, ):
        print(self.transactions)


account = ATM(1000, 0.001)
transaction_type = input('what type of transaction would you like to do?: (deposit or withdrawal):')
transaction_amount = int(input('for what amount?:'))
transaction_receipt = ''
transaction_list = []  # Create a list of strings to keep track of the transactions


if transaction_type == 'deposit':
    account.deposit(transaction_amount)
    account.get_balance()
    account.print_transactions(transaction_type, transaction_receipt)

if transaction_type == 'withdraw':
    account.check_withdraw()
    account.withdraw()
    account.get_balance()
    print_transactions()

print(account.get_balance())