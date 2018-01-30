"Lab 6: Password Generator Version 2"
import random

#n = int(input('Enter the number nput('Enter the number nput('Enter the number nput('Enter the number nput('Enter the number of characters you would like your password to be: '))

def randompassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 12
    return ''.join(random.choice(chars) for x in range(size))


print(randompassword())