"""
Lab 21
Yay, reading!
"""

import string
import random

valid_letters = string.ascii_lowercase

# path = 'files/heart_of_darkness.txt'                    # program chooses book
path = input("Enter the path of the book to open: ")    # user chooses book
novel = input("What is the name of the book? ")     # this is supposed to be italics...
author = input("Who is the author? ")


# All the functions (so many functions)


def load():
    with open(path, 'r') as f:
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


def count_words(book):
    for i in range(len(book)):
        if book[i] not in word_dict:
            word_dict[book[i]] = 1
        elif book[i] in word_dict:
            word_dict[book[i]] += 1

    return word_dict


def random_word():
    return random.choice(words_list)


def make_pairs(book):
    pairs = []
    for i in range(len(book) - 1):
        pair = [book[i], book[i + 1]]
        pairs.append(pair)

    return pairs


def count_pairs(book):
    for i in range(len(book)):
        if tuple(book[i]) not in pairs_dict:
            pairs_dict[tuple(book[i])] = 1
        elif tuple(book[i]) in pairs_dict:
            pairs_dict[tuple(book[i])] += 1

    return pairs_dict


def count_matches(book):
    for i in range(len(book)):
        if tuple(book[i]) not in match_dict:
            match_dict[tuple(book[i])] = 1
        elif tuple(book[i]) in match_dict:
            match_dict[tuple(book[i])] += 1

    return match_dict


words_list = load()

print(f"\nDid you know that {novel} by {author} has {len(words_list)} words? Neat!")

# make a list of 0's set to len(words_list)
# count_list = [0 for i in range(len(words_list))]
# not actually necessary

word_dict = {}


count_words(words_list)

print("The most frequent words are:")

tup_words = list(word_dict.items())  # list of tuples
tup_words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(tup_words))):  # print the top 10 words, or all of them, whichever is smaller
    print(f"'{tup_words[i][0]}' is found {tup_words[i][1]} times")

print(f"\nA random word found in {novel} is: {random_word()}")


# Version 2

# Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.
pairs_list = make_pairs(words_list)
pairs_dict = {}
pairs = count_pairs(pairs_list)

print("\nThe most frequent pairs of words are:")

tup_pairs = list(pairs.items())  # list of tuples
tup_pairs.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(tup_pairs))):  # print the top 10 words, or all of them, whichever is smaller
    print(f"'{' '.join(tup_pairs[i][0])}' is found {tup_pairs[i][1]} times")


# Version 3

# Let the user enter a word, then show the words which most frequently follow it.

print(f"\nNow let's see what words most frequently follow a word in {novel}. Enter a word:")
user_word = input("> ")


# match_list = [] # can make list comprehension?

match_list = []

for i in range(len(pairs_list)):
    if user_word == pairs_list[i][0]:
        match_list.append(pairs_list[i])

match_dict = {}

matches = count_matches(match_list)

print(f"\nThe words most frequently following {user_word} are:")

tup_matches = list(matches.items())  # list of tuples
tup_matches.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(tup_pairs))):  # print the top 10 words, or all of them, whichever is smaller
    print(f"'{tup_matches[i][0][1]}' follows {user_word} {tup_matches[i][1]} times")
