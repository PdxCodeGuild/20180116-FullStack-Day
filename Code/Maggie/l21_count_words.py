# Word frequency count from a given text file input
from random import choice


sherlock = 's_holmes.txt'
whit = 'w_whit_leaves.txt'
liz = 'f_lizst_let.txt'
default_path = f'/Users/magdalene/PyFiles/CodeGuild/2018coursework/Code/Maggie/resources/'


def prepare_text(text_file):  # import text file, clean up, (opt) extra cleanup, returns a list of words
    file_path = default_path + text_file
    with open(f'{file_path}', mode='r') as f:
        lines = ' '.join(f.readlines()).lower()
    punct = '!"#$%()&*+,-./:;<=>?@[\]^_`{|}~'
    trans_table = str.maketrans({key: None for key in punct})
    trans_text = lines.translate(trans_table)
    strip_text = ' '.join(trans_text.split())
    word_list = strip_text.split(' ')
    return word_list


def get_word_freq(w_list, remove_common=True):  # returns a dictionary, opt with common words removed
    with open(f'{default_path}1-1000.txt', mode='r') as f:
        lines = ' '.join(f.readlines()).lower()
    common_list = (lines.split('\n '))
    word_freq = {}  # dictionary init
    for word in w_list:
        if remove_common:
            if word not in common_list:  # remove most common words
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
    for i in range(min(5, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        sorted_words.append(words[i])
    return sorted_words  # This is a tuple!


def get_next_word(first_word, word_list):
    next_word_list = []
    for i in range(len(word_list) - 1):
        if word_list[i] == first_word:
            next_word_list.append(word_list[i + 1])
    next_word_freq_tup_list = get_word_freq(next_word_list, False)  # a list of tuples, sorted
    next_word = choice(next_word_freq_tup_list)[0]
    return next_word


def construct_str(text, first_word, output_length=30):
    cleaned_text_list = prepare_text(text)
    constructed_str = first_word
    for c in range(output_length):
        next_in_seq = get_next_word(first_word, cleaned_text_list)
        constructed_str += " " + next_in_seq
        first_word = next_in_seq
    return constructed_str


chosen_text = whit
random_first = choice(prepare_text(chosen_text))
print(construct_str(chosen_text, random_first))

# TODO: http://www.nltk.org/ natural language.. return valid sentences
