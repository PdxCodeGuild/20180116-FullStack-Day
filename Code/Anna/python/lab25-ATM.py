"""
Lab 25
Automatic Teller Machine Machine
"""

from datetime import datetime
now = datetime.now()


class ATM:
    """This is our ATM class that does ATM-type things"""

    def __init__(self, account_holder, balance=0.00, interest_rate=0.1):
        """Initialize ATM attributes"""
        self.account_holder = account_holder
        self.balance = round(balance, 2)
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        """Checks the current balance"""
        return f"Your current balance is: ${self.balance}"

    def deposit(self, amount):
        """Adds the deposit to the current balance"""
        self.balance += amount
        self.transactions.append(f"{self.account_holder} deposited ${amount} on {now.strftime('%Y-%m-%d at %H:%M:%S')}.")
        return f"You have deposited ${amount}. Your current balance is: ${round(self.balance, 2)}"

    def check_withdrawal(self, amount):
        """Checks if a withdrawal is possible"""
        if amount > self.balance:
            return "You have sufficient funds for this withdrawal."
        else:
            return f"You have insufficient funds. Your current balance is: ${round(self.balance, 2)}"

    def withdraw(self, amount):
        """Withdraws the amount from the current balance"""
        if amount < self.balance:
            self.balance -= amount
            self.transactions.append(f"{self.account_holder} withdrew ${amount} on {now.strftime('%Y-%m-%d at %H:%M:%S')}.")
            return f"You have withdrawn ${amount}. Your current balance is: ${round(self.balance, 2)}"
        else:
            return f"You have insufficient funds. Your current balance is: ${round(self.balance, 2)}"

    def calc_interest(self):
        """Calculates the interest rate on the current balance"""
        self.balance += self.balance * self.interest_rate
        return f"Your current interest rate is {self.interest_rate}%. Your current balance is: ${round(self.balance, 2)}"

    # Version 2
    def print_transactions(self):
        """Prints from a list of all previous transactions"""
        return "These are your past transactions:\n\t" + '\n\t'.join(self.transactions)


my_atm = ATM("Anna", 500.95, 0.5)

# print(my_atm.check_balance())
# print(my_atm.withdraw(100))
# print(my_atm.check_balance())
# print(my_atm.deposit(650))
# print(my_atm.check_balance())
# print(my_atm.withdraw(1500))
# print(my_atm.deposit(250))
# print(my_atm.calc_interest())
# print(my_atm.print_transactions())


# Version 3

def user_input():
    print("Welcome to your Generic™ ATM. Would you like to deposit, withdraw, check balance, or check history today?")
    inp = input("> ")
    return inp


def use_atm(choice):
    if choice == 'deposit':
        print("How much would you like to deposit?")
        amount = float(input("> "))
        print(my_atm.deposit(amount))
        again = input("Would you like to complete another transaction? y/n ")
        if again == 'y':
            choice = user_input()
            use_atm(choice)
        else:
            print("Goodbye!")
    elif choice == 'withdraw':
        print("How much would you like to withdraw?")
        amount = float(input("> "))
        print(my_atm.withdraw(amount))
        again = input("Would you like to complete another transaction? y/n ")
        if again == 'y':
            choice = user_input()
            use_atm(choice)
        else:
            print("Goodbye!")
    elif choice == 'check balance':
        print(my_atm.check_balance())
        again = input("Would you like to complete another transaction? y/n ")
        if again == 'y':
            choice = user_input()
            use_atm(choice)
        else:
            print("Goodbye!")
    elif choice == 'check history':
        print(my_atm.print_transactions())
        again = input("Would you like to complete another transaction? y/n ")
        if again == 'y':
            choice = user_input()
            use_atm(choice)
        else:
            print("Goodbye!")
    else:
        print("That is not a valid option.")
        again = input("Would you like to complete another transaction? y/n ")
        if again == 'y':
            choice = user_input()
            use_atm(choice)
        else:
            print("Goodbye!")


choice = user_input()
use_atm(choice)
