

with open('37841-0.txt', 'r') as human:
        contents = human.read()

table = str.maketrans(",.?!*#/;:", 9 * " ")
contents.translate(table)

words = contents.lower().split()

pairDictionary = dict()

for i in range(len(words)-1):
    pairs = (words[i], words[i+1])
    if words[i] in pairDictionary:
        pairDictionary[pairs] += 1
    else:
        pairDictionary[pairs] = 1

pair = list(pairDictionary.items())
pair.sort(key=lambda tup: tup[1], reverse=True)

for i in range(min(100, len(pair))):
    print(pair[i])







