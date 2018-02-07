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
    decrypt(encrypted, rotation)


def cipher(my_str, rot):
    print(my_str)
    print('Ok. Converting.')
    sleep(1)
    encrypted = ''  # empty string for the converted word
    for i in range(len(my_str)):  # find letter in the alpha list
        try:
            # TODO  add support for upper and lower characters with string.isupper()
            encrypted += (alpha_list[(((alpha_list.index(my_str[i].upper())) + rot) % 26)])  # rotate by amt
            print('.', end=' ')
        except ValueError:
            encrypted += my_str[i]
    print('Done!!')
    sleep(1)
    print('\nYour rotated word is: ', encrypted)
    return encrypted


def decrypt(encr, rota):
    print('would you like to decrypt this word?')
    ans = input().upper()
    if ans == 'Y':
        rota = -int(rota)
        return cipher(encr, rota)


print('Caeser Cipher\nThis program will encrypt a word by a cipher rotation\n')


main()
