import string

word_pairs_dictionary = dict()
long_word_list = []
word_chars = str(string.ascii_letters) + str(string.digits) + '-' + ' '


file_name = input('File name please?')




with open(file_name, 'r') as word_file:
    for line in word_file:
        line = line.strip().lower()
        for char in line:
            if char not in word_chars:
                line = line.replace(char,'')
        long_word_list.extend(line.split())



for i in range(len(long_word_list)-1):
    word_pair = (long_word_list[i], long_word_list[i+1])
    if word_pair in word_pairs_dictionary:
        word_pairs_dictionary[word_pair] += 1
    else:
        word_pairs_dictionary[word_pair] = 1



words_pairs = list(word_pairs_dictionary.items())
words_pairs.sort(key=lambda tup: tup[1], reverse=True)
for i in range(10):
    print(words_pairs[i])