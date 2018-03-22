import time


#Palindrome
magic = input('Enter a word ')
if magic == magic[::-1]:
        print('This word is a palindrome')
else:
    print('This word is not a palindrome')

#------------------------------------------------------------------------------------------------------------

#Anagram
fentry = input('Enter your first word: ')
time.sleep(0.5)
sentry = input('Enter your second word: ')
fentry = list(fentry)
sentry = list(sentry)
fentry.sort()
sentry.sort()

if fentry == sentry:
    print('These words are anagrams')
else:
    print('These words are not anagrams')