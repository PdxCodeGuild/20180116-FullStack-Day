# Define character sets as strings
# Lowercase letters will rotate to lower case and uppercase letters to upper case letters
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers = 'abcdefghijklmnopqrstuvwxyz'


def create_rotation_tables(o, n):
    # o is character list
    # n is rotation amount
    # Returns string of rotated characters
    s = ''
    s = o[n:26] + o[0:n-1]
    return s

def encrypt(s):
    pass

def decrypt(s):
    pass


print('Hello! Welcome to the ROT13 encrypter')
message = input('Please enter your secret message. ')
# Asks for an integer to rotate with, any integer will do since it will be reduced mod 26
while True:
    rotation = input('Enter the rotation.')
    try:
        rotation = int(rotation)
        break
    except ValueError:
        print ('Enter an integer please.')


rotation = rotation % 26
derotation = 26 - rotation

# Get rotated strings of upper and lower case letters
rotated_uppers = create_rotation_tables(uppers, rotation)
print(rotated_uppers)
rotated_lowers = create_rotation_tables(lowers, rotation)
print(rotated_lowers)

#  the message by finding the index of original character lists and pulling
# that index from rotated list.
# Then append that character to encoded message
# Numbers and special characters are appended as is.
rotated_message = ''
for char in message:
    if char.isupper():
        rotated_message += rotated_uppers[uppers.index(char)]
    elif char.islower():
        rotated_message += rotated_lowers[lowers.index(char)]
    else:
        rotated_message += char

print(rotated_message)