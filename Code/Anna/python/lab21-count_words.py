"""
Lab 21
Yay, reading!
"""

import string

valid_letters = string.ascii_lowercase


def load():
    with open('files/heart_of_darkness.txt', 'r') as f:
        contents = f.read().lower()
        stripped = contents.translate(string.punctuation)
        for char in stripped:
            if char not in valid_letters:
                stripped = stripped.replace(char, ' ')
        words = stripped.split(' ')
        while '' in words:
            words.remove('')
        for i in range(len(words)):         # because proper grammar is important
            if words[i] == 'i':
                words[i] = 'I'
    return words


words_list = load()
print(words_list)
print(len(words_list))
novel = "'Heart of Darkness'"
author = "Joseph Conrad"
print(f"\nDid you know that {novel} by {author} has {len(words_list)} words? Neat!")

# make a list of 0's set to len(words_list)
# count_list = [0 for i in range(len(words_list))]

word_dict = {}


def count_words(book):
    for i in range(len(book)):
        if book[i] not in word_dict:
            word_dict[book[i]] = 1
        elif book[i] in word_dict:
            word_dict[book[i]] += 1

    return word_dict


count_words(words_list)

print("The most frequent words are:")

words = list(word_dict.items()) # list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(f"'{words[i][0]}' is found {words[i][1]} times")


# count = {words_list[i]: 0 for i in range(len(words_list))}
# print(count)

