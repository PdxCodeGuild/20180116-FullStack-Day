
userInput = 'helloolleh'

def check_palindrome(palindrome):
     compared_string = palindrome[::-1]
     if palindrome == compared_string:
         return True

     return False

# Palindrome


if check_palindrome(userInput):
    print(f'\'{userInput}\' is a palindrome')
else:
    print(f'\'{userInput}\' is not a palindrome')


# Anagram
# Convert each word to lower case (lower)
# Remove all the spaces from each word (replace)
# Sort the letters of each word (sorted)
# Check if the two are equal


def check_anagram(first_word, second_word):
    is_anagram = False
    f = sorted(first_word.lower().replace(' ',''))
    s = sorted(second_word.lower().replace(' ',''))

    if len(f) != len(s):
        print(f'\'{first_word}\' and \'{second_word}\' are not anagrams')
    else:
        for i in range(len(f)):
            if f[i] == s[i]:
                is_anagram = True
            else:
                is_anagram = False

    if is_anagram:
        print(f'\'{first_word}\' and \'{second_word}\' are anagrams')

    return


first_word = 'alskd jf'
second_word = 'jf dk las'
check_anagram(first_word, second_word)

