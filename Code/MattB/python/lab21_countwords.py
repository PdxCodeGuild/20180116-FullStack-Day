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

    words = {}

    for k in range(len(book)):
        if book[k] not in words:
            words[book[k]] = 1
        else:
            words[book[k]] += 1

    del words['']

    words = list(words.items())  # list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

