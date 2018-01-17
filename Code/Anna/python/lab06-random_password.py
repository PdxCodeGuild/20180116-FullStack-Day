"""
Lab 6
Random password generator!
"""

import random
import string

print("Quick, you need a password! How many characters do you want it to be?")
n = int(input("> "))
x = 0
password = ''
choices = string.ascii_letters + string.digits

while x < n:
    password = password + random.choice(choices)
    x += 1

print(f"Here is your password: {password}")
