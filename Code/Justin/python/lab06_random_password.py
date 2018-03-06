import random

all_specials = '!@#$%^&*()'
all_nums = '1234567890'
all_lowers = 'abcdefghijklmnopqrstuvwxyz'
all_uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def choose_length(s):
    while True:
        try:
            n = int(input(s))
            break
        except ValueError:
            print ("Try again, please.")
    return n

specials_count = choose_length('How many special characters? ')
numbers_count = choose_length('How many numbers? ')
uppers_count = choose_length('How many upper case letters? ')
lowers_count = choose_length('How many lower case letters? ')

char_list = []

for i in range(specials_count):
    char_list.append(random.choice(all_specials))

for i in range(numbers_count):
    char_list.append(random.choice(all_nums))

for i in range(uppers_count):
    char_list.append(random.choice(all_uppers))

for i in range(lowers_count):
    char_list.append(random.choice(all_lowers))

print(char_list)

random.shuffle(char_list)
print(char_list)

password = ''
for i in char_list:
    password += i

print(password)


