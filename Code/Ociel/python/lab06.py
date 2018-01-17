import random
import string

length = input("Please enter the length of the password that you want: ")

letters = string.ascii_lowercase
numbers = string.digits

i = 0
password = ""

while i < int(length):
    password += letters[random.randint(0,25)]
    i += 1

print(f"This is your password: {password}")









