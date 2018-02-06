"""
Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list
saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing
out the list of transactions.
"""

""" Versions 1, 2 and 3 included"""

class ATM:
    def __init__(self, balance, interest_rate):
        self.__balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def get_balance(self):
        """ check_balance() returns the account balance """
        return self.__balance

    def deposit(self, transaction_amount):  # do I need to use amount, or can this be anything?
        """ deposit(amount) deposits the given amount in the account """
        self.__balance += transaction_amount
        self.transactions.append(f'user deposited ${transaction_amount}')
        return self.__balance

    def check_withdraw(self, transaction_amount):
        """ check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative """
        if self.__balance - transaction_amount >= 0:
            return True

    def withdraw(self, transaction_amount):
        """ withdraw(amount) withdraws the amount from the account and returns it """
        if self.check_withdraw(transaction_amount):
            self.__balance -= transaction_amount
            self.transactions.append(f'user withdrew ${transaction_amount}')
        return self.__balance

    def calc_interest(self):
        """ calc_interest() returns the amount of interest calculated on the account """
        self.__balance += self.__balance * self.interest_rate

    # function that prints out the list of transactions
    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)


account = ATM(1000, 0.001)
transaction_type = input('what would you like to do?: (deposit, withdraw, check balance, history, or calculate interest?):')
interest = 0

while transaction_type != 'done':
    if transaction_type == 'deposit':
        transaction_amount = int(input('for what amount?:'))
        account.deposit(transaction_amount)
        account.get_balance()
        account.print_transactions()
    if transaction_type == 'withdraw':
        transaction_amount = int(input('for what amount?:'))
        account.check_withdraw(transaction_amount)
        if account.check_withdraw(transaction_amount):
            account.withdraw(transaction_amount)
            account.get_balance()
            account.print_transactions()
        else:
            print('not enough money in your account to make withdrawal')
    if transaction_type == 'history':
        account.print_transactions()
    if transaction_type == 'calculate interest':
        account.calc_interest()
        #print(f'Interest: {account.interest_calculated}')


    print(f'current balance: $ {account.get_balance()}')
    transaction_type = input('what would you like to do?: (deposit, withdraw, check balance, history, calculate interest, or "done"?):')

print('thank you for using this ATM')

# interest = account.calc_interest(account.__balance, account.interest_rate)