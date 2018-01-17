"""
Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.
"""
import random

#ask the user for the length of the password

passwordLength = int(input('Enter the number of digits you would like your password to be: '))

x = 0

while x < passwordLength:
    letter = ''
    letter = random.choice("abcdefghijklmnopqrstuvwxyz") #single and double quotes both work
    print(letter)
    x += 1

