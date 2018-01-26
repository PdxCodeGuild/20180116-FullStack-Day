"""
Open the file.
Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts. You can do that with the code below.
"""
import string

f = open('80days.txt')  # open the file
contents = f.read()  # read the contents
#print(contents)
f.close()

allwords = [x for x in contents.split(' ')]
#print(allwords)


#for loops to remove spaces, punctuation, and blanks
for i in range(len(allwords)): #here we're iterating by index
    allwords[i] = allwords[i].lower()
    for char in string.punctuation: #here we're iterating by ...
        allwords[i] = allwords[i].replace(char, '')

counter = {}
for i in range(len(allwords)):
    if allwords[i] in counter.keys():
        counter[allwords[i]] += 1
    else:
        counter[allwords[i]] = 1 #note: automatically creates a key for an assignment






print(allwords)
