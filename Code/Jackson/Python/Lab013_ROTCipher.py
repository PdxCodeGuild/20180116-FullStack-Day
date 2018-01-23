"""
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the
corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so
encryption is the same as decryption.
"""

word = input('enter a word and I will encrypt it: ')
new_word = ''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', \
            't', 'u', 'v', 'w', 'x', 'y', 'z']



for char in word:
    #print(char) #check
    #print(alphabet.index(char)) #check

    # add 13 to the index
    x = alphabet.index(char) + 13
    #print(x) #check

    # if the new index is greater than 26, subtract 26
    if x > 26:
        x -= 26

    # find the character in alphabet at that index
    y = alphabet[x]
    #print(y) #check worked

    # add that character to the output to create new word
    new_word += y

print(new_word)