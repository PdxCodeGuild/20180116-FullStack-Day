# ROT13 LAB V1: TEXT ENCODER/ DECODER!

user_string_in = ''
print('\nhello!\ni will be encrypting your text for you using ROT13 format!\n')
user_string_in = user_string_in.lower()
user_string_in = input('please enter any text you would like encrypted below:\n\n:')
user_string_out = ''


def rot13(user_string_in):
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	alpha_rotate = 'nopqrstuvwxyzabcdefghijklm'

	user_string_out = ''
	for char in user_string_in:
		index = alpha.find(char)
		user_string_out += alpha_rotate[index]
	return user_string_out


print('your newly encrypted text is:\n', rot13(user_string_in))
