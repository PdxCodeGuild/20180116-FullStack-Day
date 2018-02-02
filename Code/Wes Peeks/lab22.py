import string
import math

with open('Thus Spoke Zarathrustra.txt', 'r', encoding="utf8") as book:
    contents = book.read()
    characters = (len(contents))
    sentences = contents.split('.')
    words = list(contents)


print(words)
print(sentences)
print(characters)
