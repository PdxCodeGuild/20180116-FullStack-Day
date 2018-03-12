import string

with open('Music as a Language by Ethel Home.txt', 'r') as book:  # Open the file.
	book = book.read()

book = book.lower()  # everything lowercase

zero_punctuation = str.maketrans('', '', string.punctuation)  # strip punctuation
book = book.translate(zero_punctuation)

words_list = list(book.split())  # split into a list of words

word_count_dictionary = {}  # dictionary

for word in words_list:
	if word not in word_count_dictionary.keys ():  # if a word isnt in the dictionary yet...
		word_count_dictionary[word] = 1  # add it w an increment of 1
	else:  # or else if a word is already in the dictionary...
		word_count_dictionary[word] = word_count_dictionary[word] + 1  # increment count by 1 w/o adding it in

pair_count_dictionary = {}
current_index = 0  # create pairs by tracking index in words list
for word in words_list[:-1]:  # for every word in words_list except the last
	pair = (word, words_list[current_index + 1])  # pair is tuple of (current word, word after current word)
	if pair in pair_count_dictionary.keys (): # if a pair is already in the dict keys
		pair_count_dictionary[pair] += 1 # increment count by 1
	else:
		pair_count_dictionary[pair] = 1 # otherwise its the first instance of that pair
	current_index += 1  # increment current index

word_counts = list(word_count_dictionary.items())  # list of tuples
word_counts.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count

print("\ntop 10 words:")
for word in range(min(10, len(word_counts))):  # print top 10 words, or all, whichever is smaller
	print(word_counts[word])

pair_counts = list(pair_count_dictionary.items())  # list of tuples
pair_counts.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count

print("\ntop 10 pairs:")
for pair in range(min(10, len(pair_counts))):  # print top 10 pairs, or all, whichever is smaller
	print(pair_counts[pair])
