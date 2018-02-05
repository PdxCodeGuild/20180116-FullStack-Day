import datetime

print("Welcome to the ATM of heroes!")

class ATM:
    pass

    def __init__(self, something, something_else ):  # Not really sure what should go here, if anything.
        pass

    def balance(self, deposit):
        self.balance += deposit
        return self.balance

    @staticmethod
    def interest():
        enter_interest = input("Would you like to enter in an interest? y or n?")
        if enter_interest = 'y':
            rate = input("What is the interest rate?\n:")
        else:
            rate = 0.1
        return rate

    def account_holder(self, username):


    def account(self, account_holder, balance): # account holder name, sub accounts,
        pass

    def calculate_interest(self, balance, rate):
        new_balance = balance * rate
        return new_balance

    def print_transactions(self, balance, transaction_amount):
        self.balance += transaction_amount
        print(f'This is your transaction amount {transaction_amount}.)
        print(f'This is your new balance {balance}')

