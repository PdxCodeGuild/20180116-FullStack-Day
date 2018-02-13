# Problem 1 Get a string from the user, print out another string, doubling every letter.

text = input("Enter some words: ")
original = []

for i in range(len(text)):
    original.append(text[i])
    original.append(text[i])
    i += 1

print(''.join(original))


# Problem 2 Write a function that takes a string, and returns a list of strings, each missing a different character.

import random
word_list = []


def missing_char(word):
    list_word = list(word)
    i = random.randint(0, len(word)-1)
    list_word.pop(i)
    return ''.join(list_word)


for i in range(6):
    word_list.append(missing_char('kitten'))

print(word_list)


# Problem 3 Return the letter that appears the latest in the english alphabet.

# >>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
# the latest letter is v.

import string
alphabet = list(string.ascii_lowercase)
alphabet.reverse()


def latest_letter(word):
    list_word = list(word)
    while True:
        for i in range(len(list_word)):
            for j in range(len(alphabet)):
                if list_word[i] == alphabet[j]:
                    latest = list_word[i]
                    print(f"The latest letter is: {latest}")
                    return latest


latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')

# Problem 7 Return the number of letter occurances in a string.


def count_letter(letter, word):
    list_word = list(word)
    letter_count = 0
    for i in range(len(list_word)):
        if list_word[i] == letter:
            letter_count += 1
    print(f"The letter {letter} appears in {word} {letter_count} times.")
    return letter_count


count_letter('i', 'antidisestablishmentterianism')
count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')

# Problem 8 Convert input strings to lowercase without any surrounding whitespace.


def lower_case(word):
    no_spaces = word.strip()
    return no_spaces.lower()


print(lower_case("SUPER!"))
print(lower_case("        NANNANANANA BATMAN        "))


# Problem 9 Write a function that returns the number of occurrences of 'hi' in a given string.

def count_hi(word):
    list_word = list(word)
    count = 0
    for i in range(len(list_word)):
        if list_word[i] == 'h' and list_word[i+1] == 'i':
            count += 1
    print(f"'hi' appears in {word} {count} times.")
    return count


count_hi('hihi')


# Problem 10 Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

def cat_dog(word):
    list_word = list(word)
    cat_count = 0
    dog_count = 0
    for i in range(len(list_word)):
        if list_word[i] == 'c' and list_word[i+1] == 'a' and list_word[i+2] == 't':
            cat_count += 1
    for i in range(len(list_word)):
        if list_word[i] == 'd' and list_word[i+1] == 'o' and list_word[i+2] == 'g':
            dog_count += 1
    if cat_count == dog_count:
        return True
    else:
        return False


print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('catdogcatdog'))