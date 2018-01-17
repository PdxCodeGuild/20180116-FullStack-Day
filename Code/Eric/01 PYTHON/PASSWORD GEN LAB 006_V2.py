#VERSION 2: USER CAN SELECT CHARACTER LENGTH OF RANDOMIZED PASSWORD

import random
import string

char_list = (string.printable)
password = ""

length = input("password length?\n\n:")
for x in range(0, int(length)):
	password = password + random.choice(char_list)
	while password == " " or password == "\n":  # to exclude spaces or "enter"
		password = random.choice(char_list)
print("Your password is \n\n:" + "'" + password + "'" + "\n")
