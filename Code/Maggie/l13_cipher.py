import string
from time import sleep

# ROT CIPHER
# Prompts the user for a string
# encodes string with ROT13.
#   For each character,
#       find the corresponding character,
#       add it to an output string.
# Notice that there are 26 letters in the English language, so encryption is the same as decryption.

alpha_list = list(string.ascii_uppercase)

# TBD  add support for upper and lower..

def main():
    print('First, enter a word')
    word = input('Your word: ')
    print('Your word was:', word)
    print('Next, enter a number to rotate the alphabet')
    rotation = input('Cipher amount: ')
    try:
        rotation = int(rotation)
    except ValueError:
        print('enter a valid number')
    encrypted = cipher(word, rotation)
    print(decrypt(encrypted, rotation))


def cipher(my_str, rot):
    print(my_str)
    print('Ok. Converting.')
    sleep(1)
    print('Your rotated word is:')
    encrypted = ''  # empty string for the converted word
    for i in range(len(my_str)):
        # find letter in the alpha list
        try:
            encrypted += (alpha_list[(((alpha_list.index(my_str[i].upper())) + rot) % 26)])  # rotate by amt
            print('#', i, encrypted, rot)
        except:
            encrypted += my_str[i]
    return encrypted


def decrypt(encr, rota):
    print('would you like to decrypt this word?')
    ans = input().upper()
    if ans == 'Y':
        print(rota)
        rota = -int(rota)
        print(rota)
        return cipher(encr, rota)


print('Ceaser Cipher\nThis program will encrypt a word by a cipher rotation\n')

main()
