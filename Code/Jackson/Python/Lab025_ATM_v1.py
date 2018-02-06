"""
Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account
will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following
functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account

"""


# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created
# account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the
# following functions:


class ATM:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate


    def get_balance(self):
        """ check_balance() returns the account balance """
        return self.balance

    def deposit(amount):  # do I need to use amount, or can this be anything?
        """ deposit(amount) deposits the given amount in the account """
        account.balance += amount


    def withdrawal(amount):
        """ check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative """
        if account.balance() - amount > 0:
            return True


    def withdraw(self, amount):
        """ withdraw(amount) withdraws the amount from the account and returns it """
        if self.withdrawal(amount):
            self.balance -= amount
        return amount


    def calc_interest(self, amount, interest_rate):
        """ calc_interest() returns the amount of interest calculated on the account """
        interest_calculated = account.interest_rate * account.amount

        return self.interest_calculated


amount = 10
account = ATM(1000, 0.001)  # 0.1% represented as a decimal
print(account.get_balance())

account.deposit(amount)

print(account.get_balance())



# print(account.interest_rate)
# print(type(account))
