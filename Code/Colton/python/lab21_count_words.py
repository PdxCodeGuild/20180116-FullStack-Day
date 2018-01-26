import string

with open('book.txt', 'r') as f:
    contents = f.read().lower()
    for c in string.punctuation:
        contents = contents.replace(c, ' ')


print(contents)