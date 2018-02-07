import nltk.data, nltk.tag
from nltk.tokenize import sent_tokenize, word_tokenize, MWETokenizer
from random import choice, randint
sherlock = 's_holmes.txt'
whit = 'w_whit_leaves.txt'
liz = 'f_lizst_let.txt'
gett = 'gettysburg_address.txt'

input_text = whit
default_path = f'/Users/magdalene/PyFiles/CodeGuild/2018coursework/Code/Maggie/resources/'


def import_text(filename):  # import text file, clean up, (opt) extra cleanup, returns a list of words
    file_path = default_path + filename
    with open(f'{file_path}', mode='r') as f:
        full_text_str = ' '.join(f.readlines())
    return full_text_str

def pos_sentences(full_text_str):
    sentences_list = sent_tokenize(full_text_str)
    pos_sentences = []
    for sentence in sentences_list:
        pos_sentences.append(nltk.word_tokenize(sentence))
    # for sentence in pos_sentences:
    pos_sentences = nltk.pos_tag_sents(pos_sentences)
    return pos_sentences

def construct_str(token_sent_list):
    sentence_index = randint(0, len(token_sent_list))
    word_str = token_sent_list[sentence_index][0][0]
    p = 1  #position in sentence
    while p < len((token_sent_list)[sentence_index]):
        selection_list = []
        selection_list.append(token_sent_list[sentence_index][p][0])
        for i in range(len(token_sent_list)):
            for j in range(len(token_sent_list[i])):  # iterate through all sentences by index
                if token_sent_list[i][j][1] == token_sent_list[sentence_index][p][1]:
                    selection_list.append(token_sent_list[i][j][0])
        word_str += ' ' + choice(selection_list)
        p += 1
    return word_str

def main():
    full_text = import_text(input_text)
    analyze = pos_sentences(full_text)
    markov_str = (construct_str(analyze))
    print(markov_str)
main()




# Class Word:
#     def __init__(self, word_str, pos, freq, context):
#         self.word_str = word_str
#         self.pos = pos
#         self.freq = freq
#         self.context = context
#
#
# Class Sentence:
#     def __init__(self, framework, freq, context):
#         self.framework = framework
#         self.freq = freq
#         self.context = context
#
#
# Class Utterance:
#     def __init__(self, framework, freq, context):
#         self.framework = framework
#         self.freq = freq
#         self.context = context

