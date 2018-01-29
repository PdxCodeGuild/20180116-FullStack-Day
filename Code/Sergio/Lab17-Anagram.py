"Lab 17: Anagram"
user_word1 = input('enter the first word ')
user_word2 = input('enter the second word ')
#sorted(user_word1, user_word2)

def check_anagram(user_word1, user_word2):
    user_word1 = user_word1.lower()
    user_word2 = user_word2.lower()
    user_word1 = user_word1.replace('', '')
    user_word2 = user_word2.replace('', '')
    sorted(check_anagram(user_word1, user_word2))

print(check_anagram(user_word1, user_word1))


# def check_anagram(s):
#     # Calling sort function
#     rev =
#
#     # Checking if both string are equal or not
#     if (s == rev):
#         return True
#     return False
#
# s = 'anagram'
# ans = check_anagram(user_word1, user_word2)
#
# if ans:
#         print(user_word1 + 'and' + user_word2 + 'are anagrams ')
# else:
#         print('Your words are not anagrams ')