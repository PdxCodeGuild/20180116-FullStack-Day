#Palindrome checker

# test words
w1 = 'racecar'
w2 =  'palindrome'
# first iterate through a string


def eval_pal(word): # returns boolean palindrome or no?
    print('Forward/Reverse: ', word, '/', word[::-1])
    print('Panlindrome: ', word[::-1] == word)



# Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not.
# The procedure for comparing the two strings is as follow:
#
# Convert each word to lower case (lower)
# Remove all the spaces from each word (replace)
# Sort the letters of each word (sorted)
# Check if the two are equal
# >>> enter the first word: anagram
# >>> enter the second word: nag a ram
# >>> 'anagram' and 'nag a ram' are anagrams

def ana_check():
    print('evaluate whether two words are anagrams. ')
    word_1 = input('Type in the first word: ')
    word_2 = input('Type in the second word: ')
    print(word_1, 'vs.', word_2)
    print('Anagrams: ', sorted(word_1.lower().replace(' ', '')) == sorted(word_2.lower().replace(' ', '')))

# eval_pal(w1), eval_pal(w2)  # tests
eval_pal(input('Type in a word to evaluate whether it is a palindrome: '))

ana_check()