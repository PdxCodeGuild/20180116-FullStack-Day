"""
Lab 13
ROT Cipher
"""

import string

print("Welcome to the CIA. This is our new high-tech encryption method (really).")
print("Input your super secret code:")
message = input("> ")
message = message.lower()
rotation = 13

x = 0
alphabet = []
for x in range(0, 26):
    alphabet.append(string.ascii_lowercase[x])
    x += 1
alphabet.append(' ')
# print(alphabet)

y = 0
numbers = []
for y in range(0, 26):
    numbers.append(y)
    y += 1
numbers.append(' ')
# print(numbers)

z = 0
numberfy = {}
for z in range(0, 27):
    numberfy[alphabet[z]] = numbers[z]
    z += 1
# print(numberfy)

alphabet.pop()
numbers.pop()

a = 0
encryptor = {}
for a in range(-rotation, rotation):
    encryptor[numbers[a + rotation]] = alphabet[a]
    a += 1

# print("")
encryptor[' '] = ' '
#print(encryptor)
print("")

def encrypt(text):
    i = 0
    encrypted_message = []
    for i in range(0, len(text)):
        encrypted_message.append(text[i])
        i += 1
    # print(encrypted_message)

    coded = []
    for letter in encrypted_message:
        coded.append(numberfy[letter])
    # print(coded)

    encoded = []
    for number in coded:
        encoded.append(encryptor[number])
    # print(encoded)

    print("Your secret encoded message is: '" + ''.join(encoded) + "'")


encrypt(message)

print("\nNow enter an encrypted message to decrypt:")
new_message = input("> ")
new_message = new_message.lower()

def decrypt(text):
    i = 0
    encrypted_message = []
    for i in range(0, len(text)):
        encrypted_message.append(text[i])
        i += 1
    # print(encrypted_message)

    coded = []
    for letter in encrypted_message:
        coded.append(numberfy[letter])
    # print(coded)

    encoded = []
    for number in coded:
        encoded.append(encryptor[number])
    # print(encoded)

    print("\nYour decoded message is: '" + ''.join(encoded) + "'")

decrypt(new_message)