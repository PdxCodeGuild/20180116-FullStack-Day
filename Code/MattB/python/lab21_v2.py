remove = ['.', '\'', '*', ',', '?', '!', ':', ';', '\"', '[', ']', '_', '-', '(', ')']

contents = []

with open('book.txt', 'r', encoding="utf8") as book:
    book = book.read()
    book = book.lower()
    book = book.replace('\n', ' ')
    book = book.split(' ')

    for i in range(len(book)):
        for j in range(len(remove)):
            if remove[j] in book[i]:
                book[i] = book[i].replace(remove[j], '')

    pairs = {}

    for o in range(len(book) - 1):
        if (book[o] + ' ' + book[o + 1]) not in pairs:
            pairs[book[o] + ' ' + book[o + 1]] = 1
        else:
            pairs[book[o] + ' ' + book[o + 1]] += 1

    del pairs[' ']

    pairs = list(pairs.items())  # list of tuples
    pairs.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(pairs))):  # print the top 10 words, or all of them, whichever is smaller
        print(pairs[i])