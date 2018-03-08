import random
import string

# string.ascii_letters
# string.digits


password_list = [random.choice(string.ascii_letters), random.choice(string.ascii_lowercase), \
random.choice(string.digits), random.choice(string.hexdigits), random.choice(string.ascii_uppercase),   \
random.choice(string.ascii_letters), random.choice(string.hexdigits)]

password_string = ""

create_password = input("would you like to make a password? Yes or no?\n:")

if create_password == "yes" or create_password == "y":
  make_password = int(input("How long would you like your password to be?\n:"))
  for password in range(0, make_password):
    password_string = password_string + random.choice(password_list)
  print(password_string)
elif create_password == "no" or create_password == "n":
  print("Maybe later, then. :-) ")
else:
  print("I'm confused!")
