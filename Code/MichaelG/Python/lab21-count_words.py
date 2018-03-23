# 1. Open the file.
# 2. Make everything lowercase, strip punctuation, split into a list of words.
# 3. Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count
# of 1. If it is, increment its count.
# 4. Print the most frequent top 10 out with their counts. You can do that with the code below.






# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])