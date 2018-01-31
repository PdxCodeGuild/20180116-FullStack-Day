






def is_palindrome(s):
    return s == s[::-1]



my_str1 = input("enter a word:\n> ")

if is_palindrome(my_str1):
    print('is a palindrome...')

if my_str1 == my_str1[::-1]:
    print(f'{my_str1} is a palindrome')
else:
    print(f'{my_str1} is not a palidrome')



my_str1 = input("enter a word:\n> ").lower()
my_str2 = input("enter a word:\n> ").lower()

my_str1 = my_str1.replace(" ", "")
my_str2 = my_str2.replace(" ", "")

if sorted(my_str1) == sorted(my_str2):
    print('are anagrams.')

else:
    print('are not anagrams.')


