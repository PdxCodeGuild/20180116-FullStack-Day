"""
Lab 17
Palindrome and Anagram checker
"""

print("Enter a word:")
word = input("> ")

original = []
reverse = []


def check_palindrome(word):
    for i in range(0, len(word)):
        original.append(word[i])

    i = -1
    while i > -len(word) - 1:
        reverse.append(word[i])
        i -= 1

    print(f"The reverse of {word} is {''.join(reverse)}.")

    if original == reverse:
        return f"{word} is indeed a palindrome!"
    else:
        return f"{word} is not a palindrome."


def check_anagram(word2, word3):
    word4 = word2.lower()
    word5 = word3.lower()
    word4 = word2.replace(' ', '')
    word5 = word3.replace(' ', '')

    new_word2 = ''.join(sorted(word4))
    new_word3 = ''.join(sorted(word5))

    if new_word2 == new_word3:
        return f"Yay, {word2} and {word3} are indeed anagrams!"
    else:
        return f"Nope, {word2} and {word3} are not anagrams."



print("Do you want to check if it's a palindrome? y/n")
answer = input("> ")

if answer == 'y':
    print(check_palindrome(word))
    print("Do you want to check if two words or phrases are anagrams? y/n")
    answer = input("> ")

    if answer == 'y':
        print("Sweet! Enter two words or phrases on the next two lines:")
        word2 = input("First word > ")
        word3 = input("Second word > ")
        print(check_anagram(word2, word3))
    else:
        print("OK, maybe next time.")

else:
    print("Do you want to check if two words or phrases are anagrams? y/n")
    answer = input("> ")

    if answer == 'y':
        print("Sweet! Enter two words or phrases on the next two lines:")
        word2 = input("First word > ")
        word3 = input("Second word > ")
        print(check_anagram(word2, word3))
    else:
        print("OK, maybe next time.")




