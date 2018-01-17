#working password gen
import random
import string

def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size= 10
    return ''.join(random.choice(chars) for x in range(size,20))

print(randompassword())
