"Lab 17: Anagram"
user_word1 = input('enter the first word ')
user_word2 = input('enter the second word ')
#sorted(user_word1, user_word2)

def check_anagram(user_word1, user_word2):
    user_word1 = user_word1.lower()
    user_word2 = user_word2.lower()
    user_word1 = user_word1.replace(' ', '')
    user_word2 = user_word2.replace(' ', '')

    print(sorted(user_word1))
    print(sorted(user_word2))


    # user_word1 = list(user_word1)
    # user_word1.sort()

    return sorted(user_word1) == sorted(user_word2)

print(check_anagram(user_word1, user_word2))

