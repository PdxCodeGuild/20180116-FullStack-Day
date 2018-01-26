"""
Open the file.
Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts. You can do that with the code below.
"""
import string #to get a list of all the characters not in a word, such as "!@#$%^&*()[]{}"

f = open('80days.txt')  # open the file. file was downloaded and added to respoitory
contents = f.read()  # read the contents of the book
#print(contents)
f.close()

allwords = [x for x in contents.split(' ')]  # creating a list with every words split by spaces
#print(allwords)


# for loops to remove spaces, punctuation, and blanks
for i in range(len(allwords)):  # here we're iterating by index, whereas ...
    allwords[i] = allwords[i].lower()
    for char in string.punctuation:  # here we're iterating by character in a string
        allwords[i] = allwords[i].replace(char, '')

# creating a dictionary with the number of times a word is used
counter = {}
for i in range(len(allwords)):
    if allwords[i] in counter.keys():
        counter[allwords[i]] += 1
    else:
        counter[allwords[i]] = 1  # note: automatically creates a key for an assignment

# print(counter) #check for words and count

words = list(counter.items())  # list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])


