# AVERAGES V2: NOW WITH USER NUMBERS!
numbers_list = []
sum_running = 0
user_numbers = ''

while True:
	user_numbers = input('\nPlease enter a number or type "stop" to average\n\n:')
	if user_numbers == 'stop':
		for num in numbers_list:
			sum_running = sum_running + num
		avg = sum_running / len(numbers_list)
		avg = str(avg)
		print(f'numbers: {numbers_list}\naverage: {avg}')
	else:
		try:
			user_numbers = float(user_numbers)
			numbers_list.append(user_numbers)
		except ValueError:
			print('Please enter an integer!')
