numbers = [5, 0, 8, 3, 4, 1, 6]
sum_running = 0

#CURRENT NUMBER & RUNNING SUMS
for num in numbers:
	sum_running = sum_running + num
	print('current number is: ' + str(num))
	print('current sum is: ' + str(sum_running))

#SUM AND AVERAGE ALL NUMBERS IN LIST
avg = sum_running / len(numbers)
print(avg)