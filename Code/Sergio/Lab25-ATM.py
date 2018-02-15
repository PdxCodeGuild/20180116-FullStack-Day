"""Lab 25: ATM"""

"""Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

    check_balance() returns the account balance
    deposit(amount) deposits the given amount in the account
    check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
    withdraw(amount) withdraws the amount from the account and returns it
    calc_interest() returns the amount of interest calculated on the account
"""

"""Lab 25 : ATM"""


# ATM class with all functions
class ATM:
    def __init__(self, balance, interest=0.1):
        self.balance = balance
        self.interest = interest
        self.transactions = []

    def check_balance(self):  # checks balance
        return f"Your balance is: ${self.balance}"

    def deposit(self, amount):  # deposits to balance
        self.balance += amount
        print(f"Deposit amount: {amount}")
        return self.balance

    def check_withdrawal(self, amount):  # checks balance to see if we can withdraw
        if self.balance - amount > 0:
            return True
        else:
            print('Not enough funds to withdraw.')

    def withdraw(self, amount):  # *withdraws $$$$$$$$*
        if self.balance - amount > 0:
            return f"You have withdrawn ${amount}"
        else:
            print('Not enough funds to withdraw.')

    def calc_interest(self):
        self.balance += self.balance * self.interest
        print(f"Interest: {self.interest}%")
        return self.balance

    def print_transactions(self):
        return "Transaction history:\n\t" + '\n\t'.join(self.transactions)


# testing
checking_account = ATM(50000)
print(checking_account.check_balance())
print(checking_account.withdraw(900))
print(checking_account.check_balance())
print(checking_account.deposit(int(1000)))
print(checking_account.check_balance())
print(checking_account.withdraw(1500))  # change to ridiculously high nunber to get else statement
print(checking_account.deposit(2500))
print(checking_account.calc_interest())
