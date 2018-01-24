#  PALINDROMER
user_palindrome = input('hello! i am called the palindromer!\ni can tell you what words are or are not '
                    'palindromes!\nplease enter a word you would like to use\n\n:')


def palindromer(user_palindrome):
	if user_palindrome == user_palindrome[::-1]:
		return print(user_palindrome + ' is ' + user_palindrome[::-1] + ' backwards!\nthis IS a palindrome!\n')
	elif user_palindrome != user_palindrome[::-1]:
		return print(user_palindrome + ' is ' + user_palindrome[::-1] + ' backwards!\n'
		                                                                'this IS NOT a palindrome. =(\n')


palindromer(user_palindrome)
