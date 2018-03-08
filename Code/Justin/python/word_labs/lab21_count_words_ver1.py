import string



word_dictionary = dict()
total_words = 0
# Valid characters in words are letters, numbers, hyphens, and spaces
word_chars = str(string.ascii_letters) + str(string.digits) + '-' + ' '



file_name = input('File name please?')



with open(file_name, 'r') as word_file:
    # Read a line
    for line in word_file.readlines():
        # Strip whitespace and make lowercase
        line = line.strip().lower()
        # Replace non-valid characters with ''
        for char in line:
            if char not in word_chars:
                line = line.replace(char, '')
        # split line on spaces and add words to dictionary
        print(line.split())
        for word in line.split():
            total_words += 1
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1

print('Total words: ', total_words)
# Make a list of the dictionary items
words = list(word_dictionary.items())

# Sort the word list by the second value in tuple, the number of times the word appears
words.sort(key=lambda tup: tup[1], reverse=True)

for i in range(min(10, len(words))):
    print(words[i])

