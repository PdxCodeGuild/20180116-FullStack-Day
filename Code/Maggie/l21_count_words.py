# Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.
#
# Find a book on Project Gutenberg. Download it as a UTF-8 text file.
#
# Open the file.
# Make everything lowercase, strip punctuation, split into a list of words.
# Your dictionary will have words as keys and counts as values.
# If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
# Print the most frequent top 10 out with their counts. You can do that with the code below.
# words = list(word_set.items()) # list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])
from random import choice
import string   #translation table functionality

sherlock = 'w_whit_leaves.txt'


# currently the adv of Sherlock Holmes from Gutenberg

def prepare_text(text_file):
    # import text file, clean up, (opt) extra cleanup, returns a list of words
    default_path = f'/Users/magdalene/PyFiles/CodeGuild/2018coursework/Code/Maggie/resources/{text_file}'
    with open(f'{default_path}') as f:
        raw_text = f.read().lower()
        trans_table = str.maketrans('\n', ' ', string.punctuation)  # the default translation table for punctionation
    strip_text = raw_text.translate(trans_table)
    word_list = strip_text.split(' ')
    for word in word_list:
        if len(word) < 1:
            word_list.remove(word)
    return word_list


def get_word_freq(w_list, remove_common=True):  # returns a dictionary, opt with common words removed
    with open(f'/Users/magdalene/PyFiles/CodeGuild/2018coursework/Code/Maggie/resources/1-1000.txt', mode='r') as l:
        common_words = l.read().lower()  # 1000 most common words
    common_list = (common_words.split('\n'))
    word_freq = {}  # dictionary init
    for word in w_list:
        if remove_common:
            if word not in common_list:  # remove most common words and empty strings
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
        else:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    words = list(word_freq.items())  # list of tuples
    sorted_words = []
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        sorted_words.append(words[i])
    return sorted_words

g_counter = 0
word_string = ''
def get_next_word(first_word, word_list):
    global g_counter
    global word_string
    # get most likely next word for word entered
     # given the first word, look it up in the word list, find the next occurence
    next_word_list = []
    for i in range(len(word_list) - 1): #create a most frequent dict of first_word[i]+1
        if word_list[i] == first_word: #create a frequency dictionary of wordlist[i+1]
            next_word_list.append(word_list[i + 1])
    next_word_freq_tup_list = get_word_freq(next_word_list, False)# a list of tuples, sorted
    next_word = choice(next_word_freq_tup_list)[0]
    return next_word

def construct_str(first_word, text):
    init_str = first_word
    for c in range(50):
        next_in_seq = get_next_word(first_word, text)
        init_str += " " + next_in_seq
        first_word = next_in_seq
    return init_str

prepped_text = (prepare_text(sherlock))
frequency = get_word_freq(prepped_text)
first = choice(frequency)[0]
#nextw = get_next_word(first, prepped_text)
print(construct_str(first, prepped_text))

# TODO: http://www.nltk.org/ natural language.. return valid sentences
