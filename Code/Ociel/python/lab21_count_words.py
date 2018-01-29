# Count Words

# Reads the file and returns a dictionary with the keys and
# the value has the amount of times it was repeated.
def read_file():
    with open('words_doc.txt', 'r') as file:
        contents_of_file = file.read().lower().split()

    contents_of_file = [i.strip('.,:;!()[]#* ') for i in contents_of_file]

    dictionary = {}

    for word in contents_of_file:
        # .keys() returns all the keys inside of a dictionary.
        # it returns them into a list
        # here we say that if the word(which is a list) is in
        # the dictionary which we made into a list by adding .keys
        # then add one into the part of the value of the dictionary
        # word. SIDE NOTE: If the word is repeated it will be discarded.
        # so that means you will only have one copy of that word inside
        # dictionary.
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

# Prints the Top Ten Words.
# This bottom code was Given.
def print_file(word_set):
    words = list(word_set.items())  # list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(f'Word number {i + 1} is {words[i]}')


# Call Functions
dictionary = read_file()
print_file(dictionary)
