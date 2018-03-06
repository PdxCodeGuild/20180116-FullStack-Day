# VERSION 3: FEATURING THE ROMANS!!!

# list of roman numerals instead of dictionary makes it easier to move around here
number_dict_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
					 (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def roman_numeralize(integer):
	roman_num = ''  # roman_num starts as a blank string
	number = integer  # number value to convert = integer parameter for function
	while 0 < number:  # while the number is greater than 0
		for i, r in number_dict_roman:  # for every instance in the list roman_keys_sorted
			while number >= i:  # if the number entered is greater than or equal to the instance
				roman_num += r  # the roman_num is equal to itself plus the translation
				number -= i  # the initial number has the current index subtracted from it
	return roman_num


int_ans = False  # accounting for integer answer by starting the type status as false
number = input('\nhello! i am going to convert your number into a word for you!\n'
			   'please enter a number that you would like to convert\n\n:')

while int_ans is False:  # while the answer is not an integer
	try:
		number = int(number)  # try converting it
		int_ans = True  # and making integer status true
	except ValueError:
		number = input('please use an integer!\n:')  # if we get a value error the input wasnt actually an integer

print("the roman numeral for " + str(number) + " is: ")
print(roman_numeralize(number))
