import random

chars = '#%@(&*@ABCDEGHijklmnopqrstuv'

def choose_length():
    while True:
        try:
            n = int(input("how long is the password? "))
            break
        except ValueError:
            print ("Try again, please.")
    return n

length = choose_length()

while length > 0:
    i = 0
    password = ''
    while i < length:
        password += random.choice(chars)
        i += 1

    print(password)
    length = choose_length()

