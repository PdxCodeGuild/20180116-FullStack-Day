

# opens the file as read-only
with open('37841-0.txt', 'r') as human:
        contents = human.read()

# strips punctuation
table = str.maketrans(",.?!*#/;:", 9 * " ")
contents.translate(table)

# words are split and made lowercase
words = contents.lower().split()

# print(words)

# initializes an empty dictionary
wordDictionary = {}

# for-loop interates through the index words. if words occurances happens multiple times, the value is incremented, else occurance only happens once, it is assigned 1.
for i in range(len(words)):
    if words[i] in wordDictionary.keys():
        wordDictionary[words[i]] += 1
    else:
        wordDictionary[words[i]] = 1

# print(wordDictionary)

word = list(wordDictionary.items())
word.sort(key=lambda tup: tup[1], reverse=True)

for i in range(min(1000, len(word))):
    print(word[i])