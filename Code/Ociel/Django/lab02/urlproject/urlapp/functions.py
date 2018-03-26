from random import choice
from string import ascii_letters, digits

def create_new_code():
    new_code = ''
    for _ in range(8):
        new_code += ''.join(choice(digits + ascii_letters))
    return new_code
