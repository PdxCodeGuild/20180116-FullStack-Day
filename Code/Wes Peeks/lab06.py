import random
import string

pass_upper = string.ascii_uppercase
pass_lower = string.ascii_lowercase
pass_punc = string.punctuation

pass_list = pass_upper + pass_lower + pass_punc

password = ""

n = int(input("How long of a Password?\n:"))

i = 0

while i in range(0, int(n)):
    password = password + str(random.choice(pass_list))
    i += 1
print(password)
