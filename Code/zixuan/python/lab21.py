with open('words.txt', 'r') as f:
  contents = f.read()
contents = contents.replace(',', ' ')
contents = contents.replace('.', ' ')
contents = contents.replace('\n',' ')
contents = contents.replace('!', ' ')

words = contents.split(" ")
word_dictionaries = {}


for word in words:

    if word not in word_dictionaries:
        word_dictionaries.update({word: 1})
    else:
        word_dictionaries[word] = word_dictionaries[word]+1


word_dictionaries=sorted(word_dictionaries.items(), key=lambda d: d[1])


print(word_dictionaries)