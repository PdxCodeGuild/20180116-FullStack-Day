# Word frequency count from a given text file input
from random import choice


sherlock = 's_holmes.txt'
whit = 'w_whit_leaves.txt'
liz = 'f_lizst_let.txt'
gett = 'gettysburg_address.txt'
default_path = f'/Users/magdalene/PyFiles/CodeGuild/2018coursework/Code/Maggie/resources/'
chosen_text = liz


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


def get_input():  # allow the user to interface, select the text and first word.
    selections = {'1' : sherlock, '2' : whit, '3' : liz, '4' : gett}
    print(f'Choose a textfile to evaluate:\n\t1. {sherlock} \n\t2. {whit} \n\t3. {liz} \n\t4. {gett}')
    while True:
        u_selected_text = input('Your choice: ')
        try:
            selected_text = selections[str(u_selected_text)[0]]
            break
        except:
            print('Invalid choice. Try again.')
    print(f'Your selection is {selected_text}. What would you like to do?')
    print('you may choose:\n'
          '\t1. Get the frequency of the most common words in the text.\n'
          f'\t2. Use {selected_text} as a text primer with a random word from the text.')
    while True:
        random_first = choice(prepare_text(chosen_text))
        u_select_funct = input('Your choice: ')
        funct_d = {'1' : get_word_freq(prepare_text(selected_text)),
                   '2' : construct_str(selected_text, random_first)}
        try:
            select_funct = funct_d[str(u_select_funct)[0]]
            break
        except:
            print('Invalid choice. Try again.')
    print(select_funct)

# TODO: Let user choose the first word. Let the user choose whether to remove common.
# TODO: http://www.nltk.org/ natural language.. return only valid sentences
get_input()