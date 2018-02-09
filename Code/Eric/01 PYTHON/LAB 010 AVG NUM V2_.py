# AVERAGES V2: NOW WITH USER NUMBERS!
numbers = []
sum_running = 0
user_numbers = ''

while True:
	user_numbers = input('\nPlease enter a number or type "stop" to quit\n\n:')
	if user_numbers == 'stop':
		print('Thank you for playing! Goodbye!')
		break
	elif user_numbers is not int():
		print('Please enter an integer!')
	else:
		numbers.append(user_numbers)
	#
	# while len(numbers) > 5:
	# 	user_numbers = input('\nPlease enter a number or type "stop" to quit\n\n:')
	# 	if user_numbers is 'stop':
	# 		break

# CURRENT NUMBER & RUNNING SUMS
for num in numbers:
	sum_running = sum_running + num
	numbers.append(user_numbers)
	print('current number is: ' + str(num))
	print('current sum is: ' + str(sum_running))

# SUM AND AVERAGE ALL NUMBERS IN LIST
avg = sum_running / len(user_numbers)
avg = str(avg)
print('Your average is: ' + avg)

# COME BACK TO THIS!!!!