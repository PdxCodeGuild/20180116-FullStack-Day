"""
Lab 6
Random password generator!
"""

import random
import string

print("Quick, you need a password! How many characters do you want it to be?")

while True:
    n = input("> ")
    try:
        n = int(n)
        break
    except ValueError:
        print("Not a number!")

x = 0
password = ''
choices = string.ascii_letters + string.digits

while x < n:
    password = password + random.choice(choices)
    x += 1

print(f"Here is your password: {password}")
