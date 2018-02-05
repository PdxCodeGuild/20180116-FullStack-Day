#opened file
with open('Thus Spoke Zarathrustra.txt', 'r', encoding="utf8") as book:
    contents = book.read()

#converted to lower case and split book into lists of words
contents = contents.lower()
word_set = {}
no_pun = ''
punctuation = '/\\,.?!’\''
contents = contents.split()

for i in range(len(contents)):
    for char in punctuation:
        contents[i] = contents[i].replace(char, '')

for key in contents:
    if key not in word_set.keys():
        word_set[key] = 1
    else:
        word_set[key] += 1

words = list(word_set.items()) # list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(len(word_set), len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])






