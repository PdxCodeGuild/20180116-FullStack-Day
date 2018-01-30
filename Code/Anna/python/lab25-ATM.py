"""
Lab 25
Automatic Teller Machine Machine
"""

from datetime import datetime
now = datetime.now()


class ATM:
    """This is our ATM class that does ATM-type things"""

    def __init__(self, account_holder, balance=0, interest_rate=0.1):
        """Initialize ATM attributes"""
        self.account_holder = account_holder
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        """Checks the current balance"""
        return f"Your current balance is: ${self.balance}"

    def deposit(self, amount):
        """Adds the deposit to the current balance"""
        self.balance += amount
        self.transactions.append(f"{self.account_holder} deposited ${amount} on {now.strftime('%Y-%m-%d at %H:%M:%S')}.")
        return f"You have deposited ${amount}. Your current balance is: ${self.balance}"

    def check_withdrawal(self, amount):
        """Checks if a withdrawal is possible"""
        if amount > self.balance:
            return "You have sufficient funds for this withdrawal."
        else:
            return f"You have insufficient funds. Your current balance is: ${self.balance}"

    def withdraw(self, amount):
        """Withdraws the amount from the current balance"""
        if amount < self.balance:
            self.balance -= amount
            self.transactions.append(f"{self.account_holder} withdrew ${amount} on {now.strftime('%Y-%m-%d at %H:%M:%S')}.")
            return f"You have withdrawn ${amount}. Your current balance is: ${self.balance}"
        else:
            return f"You have insufficient funds. Your current balance is: ${self.balance}"

    def calc_interest(self):
        """Calculates the interest rate on the current balance"""
        self.balance += self.balance * self.interest_rate
        return f"Your current interest rate is {self.interest_rate}%. Your current balance is: ${self.balance}"

    # Version 2
    def print_transactions(self):
        """Prints from a list of all previous transactions"""
        return "These are your past transactions:\n\t" + '\n\t'.join(self.transactions)


my_atm = ATM("Anna", 500, 0.5)

print(my_atm.check_balance())
print(my_atm.withdraw(100))
print(my_atm.check_balance())
print(my_atm.deposit(650))
print(my_atm.check_balance())
print(my_atm.withdraw(1500))
print(my_atm.deposit(250))
print(my_atm.calc_interest())
print(my_atm.print_transactions())
