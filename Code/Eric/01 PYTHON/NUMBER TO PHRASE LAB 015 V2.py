# VERSION 2: 999!

number_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
               9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
               15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty',
               30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
               0: 'Zero'}

int_ans = False


def number_word(number):
	if 0 <= number <= 99:
		try:
			return number_dict[number]
		except KeyError:
			return number_dict[number - (number % 10)] + number_dict[number % 10]
	elif 99 < number < 1000:
		a = number // 100
		b = number % 100
		c = b // 10
		d = b % 10
		if c == 1:
			return number_dict[a] + ' Hundred', number_dict[b]
		elif c == 0:
			return number_dict[a] + ' Hundred', number_dict[d]
		else:
			c = c * 10
			if d == 0:
				return number_dict[a] + ' Hundred', number_dict[c]
			else:
				return number_dict[a] + ' Hundred', number_dict[c], number_dict[d]
	elif 1000 <= number:
		print('number entered is out of range! sorry!\n')


try:
	number = int(input('\nhello! i am going to convert your number into a word for you!\n'
	                   'please enter a number that you would like to convert\n\n:'))
	int_ans = True
except ValueError:
		number = input('please use an integer!\n:')

while int_ans is False:
	try:
		number = int(number)
		break
	except ValueError:
			number = input('please use an integer!\n:')

print(number_word(number))

