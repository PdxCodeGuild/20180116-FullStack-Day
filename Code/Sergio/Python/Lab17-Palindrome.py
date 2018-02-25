"Lab 17: Palindrome"

# function which return reverse of a string
user_word = input('type a word to check if its a palindrome: ')


# def reverse(s):
#     return s[::-1]

def isPalindrome(s):
    return s == s[::-1]


s = 'palindrome'
ans = isPalindrome(user_word)

if ans:
    print('Your word is a palindrome ')
else:
    print('Your word is not a palindrome ')
