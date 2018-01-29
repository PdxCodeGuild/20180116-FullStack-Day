"Lab 17: Palindrome"

# function which return reverse of a string
user_word = input('type a word to check if its a palindrome: ')

# def reverse(s):
#     return s[::-1]

def isPalindrome(s):
    # Calling reverse function
    rev = s[::-1]

    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False

s = 'palindrome'
ans = isPalindrome(user_word)

if ans:
        print('Your word is a palindrome ')
else:
        print('Your word is not a palindrome ')