operations_list = ['+', '-', '*', '/']

#OPERATION
while True:
	user_op = ''
	user_op = input('what operation would you like to use?\n\ntype:\n"+" for addition\n"-" for subtraction\n'
					'"*" for multiplication\n"/" for division\n\n:')
	if user_op not in operations_list:
		user_op = input('please type:\n"+" for addition\n"-" for subtraction\n"*" for multiplication\n"/" for '
						'division\n\n:')
		if user_op in operations_list:
			break
	else:
		break


#CLEAN VERSION: NUMBER INPUTS USING FUNCTION
def user_numbers():
	counter = 0
	while True:
		user_count = ''
		if counter == 0:
			user_count = 'first'
		elif counter == 1:
			user_count = 'second'
		user_num0 = input('\nwhat is your ' + user_count + ' number?\n:')
		while type(user_num0) is not float:
			try:
				user_num0 = float(user_num0)
			except ValueError:
				user_num0 = input('please use an integer\n\n:')
		break
	counter += 1
	return user_num0

user_num1 = user_numbers()
user_num2 = user_numbers()

# ALTERNATIVES***
# DIRTY VERSION: NUMBER INPUTS USING WHILE LOOPS
# #FIRST NUMBER
# while True:
# 	user_num1 = ''
# 	user_num1 = input('\nwhat is your first number?\n:')
# 	while type(user_num1) is not float:
# 		try:
# 			user_num1 = float(user_num1)
# 		except ValueError:
# 			user_num1 = input('please use an integer\n\n:')
# 	break
#
# #SECOND NUMBER
# while True:
# 	user_num2 = ''
# 	user_num2 = input('\nwhat is your second number?\n:')
# 	while type(user_num2) is not float:
# 		try:
# 			user_num2 = float(user_num2)
# 		except ValueError:
# 			user_num2 = input('please use an integer\n\n:')
# 	break

# CLEAN VERSION 2: FROM MATTHEW
# def get_number(prompt_text, error_text):
# 	while True:
# 		num = input(prompt_text)
# 		try:
# 			num = int(num)
# 			return num
# 		except ValueError:
# 			print(error_text)
#
# num1 = get_number('enter number 1', 'that is not a number')
# num2 = get_number('enter number 2', 'that is not a number')


#QUICK MATHS
if user_op == '+':
	answer = user_num1 + user_num2
	print(user_num1, '+', user_num2, '=', answer)
elif user_op is '-':
	answer = user_num1 - user_num2
	print(user_num1, '-', user_num2, '=', answer)
elif user_op is '*':
	answer = user_num1 * user_num2
	print(user_num1, '*', user_num2, '=', answer)
elif user_op is '/':
	answer = user_num1 / user_num2
	print(user_num1, '/', user_num2, '=', answer)
