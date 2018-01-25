# Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.
#
# Find a book on Project Gutenberg. Download it as a UTF-8 text file.
#
# Open the file.
# Make everything lowercase, strip punctuation, split into a list of words.
# Your dictionary will have words as keys and counts as values.
# If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
# Print the most frequent top 10 out with their counts. You can do that with the code below.
# words = list(word_set.items()) # list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])

import string   #translation table functionality

punct = '.:?,-&'  # punctuation for translation table
replace = (' ' * len(punct))
trans_table = str.maketrans('\n', ' ', string.punctuation)  # the default translation table for punctionation
# strip = maketrans(trans_out, '')  # removes punctuation

with open('/Users/magdalene/PyFiles/CodeGuild/2018coursework/Code/Maggie/resources/s_holmes.txt') as f:
    # currently the adv of Sherlock Holmes from Gutenberg
    raw_text = f.read().lower()

with open('/Users/magdalene/PyFiles/CodeGuild/2018coursework/Code/Maggie/resources/1-1000.txt') as l:
    # 1000 most common words
    common_words = l.read().lower()


common_list = (common_words.split('\n'))

strip_text = raw_text.translate(trans_table)
word_list = strip_text.split(' ')
word_freq = {}

for word in word_list:
    if word not in common_list and len(word) > 0:  # remove most common words and empty strings
        if word in word_freq.keys():
            word_freq[word] += 1
        else:
            word_freq[word] = 1


words = list(word_freq.items()) # list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

