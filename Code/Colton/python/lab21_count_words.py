import string
my_dictionary = {}

with open('book.txt', 'r') as f:
    contents = f.read().lower()
    for c in string.punctuation:
        contents = contents.replace(c, ' ')
    contents = contents.split()
    for word in contents:
        if word in my_dictionary:
            my_dictionary[word] += 1
        else:
            my_dictionary[word] = 1

    words = list(my_dictionary.items())  # list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])





