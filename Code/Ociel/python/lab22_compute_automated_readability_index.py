# CRA: Compute Automated Readability Index
import math
#############################################################################
def print_CRAI(score, file):
    ari_scale = {
        1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
        2: {'ages': '6-7', 'grade_level': '1st Grade'},
        3: {'ages': '7-8', 'grade_level': '2nd Grade'},
        4: {'ages': '8-9', 'grade_level': '3rd Grade'},
        5: {'ages': '9-10', 'grade_level': '4th Grade'},
        6: {'ages': '10-11', 'grade_level': '5th Grade'},
        7: {'ages': '11-12', 'grade_level': '6th Grade'},
        8: {'ages': '12-13', 'grade_level': '7th Grade'},
        9: {'ages': '13-14', 'grade_level': '8th Grade'},
        10: {'ages': '14-15', 'grade_level': '9th Grade'},
        11: {'ages': '15-16', 'grade_level': '10th Grade'},
        12: {'ages': '16-17', 'grade_level': '11th Grade'},
        13: {'ages': '17-18', 'grade_level': '12th Grade'},
        14: {'ages': '18-22', 'grade_level': 'College'}
    }
    if score > 14:
        score = 14

    age = ari_scale[score]['ages']
    grade = ari_scale[score]['grade_level']

    print(f'The ARI for {file} is {score} '
          f'This corresponds to a {grade} level of difficulty '
          f'that is suitable for an average person {age} years old.')
#############################################################################

def CRAI_calculation(characters_size,amount_of_words,num_of_sentences):
    total_score = 4.71 * (characters_size/amount_of_words) + \
                  0.5 * (amount_of_words/num_of_sentences) - 21.43

    return math.ceil(total_score)
#############################################################################

def read_file(file):
     with open('words_doc.txt', 'r') as file:
        contents = file.read().split()
     return contents
#############################################################################

def get_word_char_sentence_amounts(contents):
    character_amount = 0
    sentence_size = 0
    sentence_enders = '.'

    # Get the number of words by stripping all punctuation characters
    words = [i.strip('!@#$%^&*()[]?>,.<:;"') for i in contents]
    words_amount = len(words)

    # Get the number of characters
    # Get the number of sentences strip() does not include '.!? '
    # those will determine the end of a sentence
    sentence = [i.strip('@#$%^&*()[]>,<:;" \'\'') for i in contents]

    for index, value in enumerate(sentence):
        # The way we get the number of sentences is by checking to see if our
        # sentence_ender is in the value(value is the each individual word inside
        # sentence minus ".?!"
        if sentence_enders in value:
            sentence_size += 1
        # The length of each character is the the amount of characters
        # that the document has
        character_amount += len(value)

    return character_amount, words_amount, sentence_size
#############################################################################
# CALLING THE FUNCTIONS
file_name = 'words_doc.txt'
file_content = read_file(file_name)
char, words, sent = get_word_char_sentence_amounts(file_content)
total_score = CRAI_calculation(char, words, sent)
print_CRAI(total_score, file_name)

