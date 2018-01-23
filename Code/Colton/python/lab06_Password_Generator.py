import random
import string
u = string.ascii_uppercase
l = string.ascii_lowercase
d = string.digits
p = string.punctuation

characters = [u, l, d, p]

password = ""
print("Let's build a password")
special_1 = input("How many upper case characters would you like?\n:")
special_2 = input("How many lower case characters would you like?\n:")
special_3 = input("How many numerical characters would you like?\n:")
special_4 = input("How many punctuation characters would you like?\n:")




for i in range(0, int(special_1)):
    password = password + random.choice(characters[0])

for i in range(0, int(special_2)):
    password = password + random.choice(characters[1])

for i in range(0, int(special_3)):
    password = password + random.choice(characters[2])

for i in range(0, int(special_4)):
    password = password + random.choice(characters[3])

password = list(password)
password = random.sample(password, len(password))

password = ''.join(password)
print(password)
