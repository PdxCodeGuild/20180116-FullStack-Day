import os
import string


with open('Frankenstein.txt', 'r') as frankenstein_file:
        contents = frankenstein_file.read()

# Make everything lowercase, strip punctuation, split into a list of words.
words = contents.lower().split()

def remove_punct(text):
    return [w.strip(string.punctuation) for w in words] # Need to understand this better. What about translate?

words = remove_punct(words)
words = remove_apostrophes(words)
words_copy = words.copy()

print(words)

word_dictionary = {}

for i in range(len(words)):
    if words[i] not in word_dictionary.keys():
        word_dictionary[words[i]] = 1
    else:
        word_dictionary[words[i]] += 1



print(word_dictionary)


words = list(word_dictionary.items()) # list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
