# import random
import string
import random

# create list of random characters

characters =  'fF!1@2#3$4%5^6&7*8ASDasdJKLjkl'

n = 0
string_build = ''

while n < 8:
    string_build += random.choice(characters)
    n += 1
print(string_build)