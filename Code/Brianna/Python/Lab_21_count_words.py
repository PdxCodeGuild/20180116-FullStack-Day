import os
import string


with open('Frankenstein.txt', 'r') as frankenstein_file:
        contents = frankenstein_file.read()

# Make everything lowercase, strip punctuation, split into a list of words.
words = contents.lower().split()

def remove_punct(text):
    return [w.strip(string.punctuation) for w in words] # Need to understand this better

words = remove_punct(words)
words_copy = words.copy()

# May be able to use zip()

print(words)

'''
word_dictionary = {}

for word_num in range(len(words)):
    new_word[] =
    word_dictionary.append(new_word)

'''

word_dictionary = make_dictionary()

print(word_dictionary)

# Your dictionary will have words as keys and counts as values.
# If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.


# Let's write a python module to analyze a given text file containing a book for its vocabulary frequency
# and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way
# to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.



# Print the most frequent top 10 out with their counts. You can do that with the code below.
'''
words = list(word_set.items()) # list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

'''
