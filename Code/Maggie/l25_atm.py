# Let's represent an ATM with a class containing two attributes:
# a balance and an interest rate.
# A newly created account will default to a balance of 0 and an interest rate of 0.1%.
# Implement the initializer, as well as the following functions:

# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account

class Atm:
    def __init__(self, balance, interest_rt):
        self.balance = balance
        self.interest_rt = interest_rt

    def check_balance(self):
        # returns account balance
        print(f'Current balance: {self.balance}')
        return (self.balance)

    def deposit(self, amount):
        # deposits into account
        self.balance += amount
        print(f'Deposit amount: {amount}')
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance - amount > 0:
            return True

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def calc_interest(self):
        self.balance += self.check_balance() * self.interest_rt / 100
        print(f'Interest: {self.interest_rt}')
        return self.balance


yr_checking_acct = Atm(0.00, 0.01)
Atm.check_balance(yr_checking_acct)
Atm.deposit(yr_checking_acct, 500.00)
Atm.check_balance(yr_checking_acct)
Atm.calc_interest(yr_checking_acct)
Atm.check_balance(yr_checking_acct)
Atm.withdraw(yr_checking_acct, 100.00)
Atm.check_balance(yr_checking_acct)