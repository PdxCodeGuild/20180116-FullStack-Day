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

counter = 0

#CLEAN VERSION: NUMBER INPUTS USING FUNCTION
def user_numbers():
	while True:
		global counter  # from here when u encounter "counter" use global var
		user_num0 = ''  # for function
		user_count = ''
		if counter is 0:
			user_count = 'first'
		elif counter is 1:
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

#DIRTY VERSION: NUMBER INPUTS USING WHILE LOOPS
#FIRST NUMBER
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

#QUICK MATHS
if user_op is '+':
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
