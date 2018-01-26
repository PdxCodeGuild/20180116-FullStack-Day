import string



word_pairs_dictionary = dict()
long_word_list = []
word_chars = str(string.ascii_letters) + str(string.digits) + ' '




file_name = input('File name please?')




with open(file_name, 'r') as word_file:
    for line in word_file:
        line = line.strip().lower()
        for char in line:
            if char not in word_chars:
                line = line.replace(char, '')

        for word in line.split():
            long_word_list.append(word)



for i in range(len(long_word_list)-1):
    word_pair = (long_word_list[i], long_word_list[i+1])
    if word_pair in word_pairs_dictionary:
        word_pairs_dictionary[word_pair] += 1
    else:
        word_pairs_dictionary[word_pair] = 1


# Ask user for a word
chosen_word = input('Enter a word to find')


# Check chosen word against first word in word pair
# Build a list of desired key, value tuples
chosen_word_pairs = []
for key in word_pairs_dictionary:
    if key[0] == chosen_word:
        key_value_pair = (key, word_pairs_dictionary[key])
        chosen_word_pairs.append(key_value_pair)


# Sort the list of chosen word pairs by number of instances
chosen_word_pairs.sort(key=lambda tup: tup[1], reverse=True)

total = 0

# Print 10 most frequent word pairs or all word pairs whichever is less
for i in range(len(chosen_word_pairs)):
    total += chosen_word_pairs[i][1]
    print(chosen_word_pairs[i])

print(total)