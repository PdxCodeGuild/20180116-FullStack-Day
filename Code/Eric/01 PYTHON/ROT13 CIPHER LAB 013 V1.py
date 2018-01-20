# For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

import string

user_string_in = ''

print('\nhello!\ni will be encrypting your text for you using ROT13 format!\n')

user_string_in = user_string_in.lower()
user_string_in = input('please enter any text you would like encrypted below:\n\n:')

for char in user_string_in[0:]:
	user_string_in = user_string_in.replace(char, string.ascii_lowercase[string.ascii_lowercase.find(char) + 13])
	user_string_out = user_string_in


print('your newly encrypted text is:\n', user_string_out)
