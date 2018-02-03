"""
Lab 21: Count Words v1. Business Hints for Men and Women (wth genders why?!)
"""
import string

dictionary = dict()  # {key: value,}
word_total = 0  # current total
chars = str(string.ascii_letters) + ' '  # characters we want to import

openbook = 'businesshints.txt'

with open(openbook, 'r') as f:
    for line in list(f):
        # removes white space and makes chars lowercase
        line = line.lower().strip()
        # calls global char
        for char in line: # replaces punctuation based on chars string, allowing only letters
            if char not in chars:
                line = line.replace(char, '')

        # splitssss words into tuples
        line.split()

        # adds to dictionary
        for word in line.split():
            word_total += 1  # incrementing by 1
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1

# total words in book using an f string
print(f"'Business Hints for Men and Women' has {word_total} total words")

# returns a list of dictionary (key, value) tuple pairs.
words = list(dictionary.items())

# assignment code #
words.sort(key=lambda tup: tup[1], reverse=True)  # list of tuples sort largest to smallest, based on count# top 10

print('The top 10 words used. ')

# keywords
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i]) # prints index of dictionary

f.close() # does this do anything?