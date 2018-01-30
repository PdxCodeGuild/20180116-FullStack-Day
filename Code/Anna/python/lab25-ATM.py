"""
Lab 25
Automatic Teller Machine Machine
"""


class ATM:
    """This is our ATM class that does ATM-type things"""

    def __init__(self, account_holder, balance=0, interest_rate=0.1):
        """Initialize ATM attributes"""
        self.account_holder = account_holder
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        """Checks the current balance"""
        return f"Your current balance is: {self.balance}"

    def deposit(self, amount):
        """Adds the deposit to the current balance"""
        self.balance += amount
        return f"You have deposited {amount}. Your current balance is: {self.balance}"

    def check_withdrawal(self, amount):
        """Checks if a withdrawal is possible"""
        if amount < self.balance:
            return "You have sufficient funds for this withdrawal."
        else:
            return f"You have insufficient funds. Your current balance is: {self.balance}"

    def withdraw(self, amount):
        """Withdraws the amount from the current balance"""
        self.balance -= amount
        return f"You have withdrawn {amount}. Your current balance is: {self.balance}"

    def calc_interest(self):
        """Calculates the interest rate on the current balance"""
        self.balance += self.balance * self.interest_rate
        return f"Your current interest rate is {self.interest_rate}. Your current balance is: {self.balance}"


my_atm = ATM("Anna", 500, 0.5)

print(my_atm.check_balance())
print(my_atm.withdraw(100))
print(my_atm.check_balance())
