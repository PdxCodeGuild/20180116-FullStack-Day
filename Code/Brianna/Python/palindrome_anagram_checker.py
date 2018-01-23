def check_palendrome(a_string):
    if word[:] == word[::-1]:
        print("This is a palendrome.")
    else:
        print("This is not a palendrome.")

word = input("Type in a word to check and see if it's a palendrome.\n:")

check_palendrome(word)


def check_anagram(first_string, second_string):
    str.lower(first_string)
    str.lower(second_string)
    first_string.replace(" ", "")
    second_string.replace(" ", "")
    first_string = ''.join(sorted(first_string))
    second_string = ''.join(sorted(second_string))
    if first_string[:] == second_string[:]:
        print("This is an anagram.")
    else:
        print("This is not an anagram.")

anagram_one = input("Type in first entry for anagram check. \n:")
anagram_two = input("Type in second entry for anagram check. \n:")

check_anagram(anagram_one, anagram_two)


