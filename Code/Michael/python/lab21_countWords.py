

with open('37841-0.txt', 'r') as human:
        contents = human.read()

table = str.maketrans(",.?!*#/;:", 9 * " ")
contents.translate(table)

words = contents.lower().split()

wordDictionary = {}

for i in range(len(words)):
    if words[i] in wordDictionary:
        wordDictionary[words[i]] += 1
    else:
        wordDictionary[words[i]] = 1

word = list(wordDictionary.items())
word.sort(key=lambda tup: tup[1], reverse=True)

for i in range(min(100, len(word))):
    print(word[i])








