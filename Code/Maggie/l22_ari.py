#ARI calculator

default_path  = f'/Users/magdalene/PyFiles/CodeGuild/2018coursework/Code/Maggie/resources/'


def prepare_text(txt_file):
    file_path = default_path + txt_file
    with open(f'{file_path}', mode='r') as f:
        lines = ' '.join(f.readlines())
    punct = '"#$%()&*+,-/:<=>@[\]^_`{|}~'  # leave stops
    trans_table = str.maketrans({key: None for key in punct})
    trans_text = lines.translate(trans_table)
    strip_text = ' '.join(trans_text.split())
    word_list = strip_text.split(' ')

    return word_list


def calc_ari(prepped_list):
    stops = '!.;?'
    sentence_count = 0 # based on number of stops
    for i in range(len(prepped_list)):  # tallying and removing stops
        for stop in stops:
            if stop in prepped_list[i]:
                sentence_count += 1
                prepped_list[i] = prepped_list[i].replace(stop, '')
    char_count = 0
    word_count = len(prepped_list)
    for i in range(word_count):
        char_count += len(prepped_list[i])
    ari = round(4.71 * (char_count/word_count) + 0.5 * (word_count/sentence_count) - 21.43)
    print(f'Sentence count: {sentence_count}\nWord Count: {word_count}\nCharacter count: {char_count}')
    return ari


def ari_lookup(calc_ari):
    ari_dict = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
    }
    index_dict = ari_dict[calc_ari]
    get_age = index_dict['ages']
    get_grade_lev = index_dict['grade_level']
    print(f'The ARI for (this text) is {calc_ari}. This corresponds to a/an {get_grade_lev} level of difficulty.')
    print(f'That is suitable for an average person of {get_age} years old.\n')


def get_ari_info(txt_file):
    print(f'Retrieving ARI for {txt_file}.')
    text_list = prepare_text(txt_file)
    ari = calc_ari(text_list)
    ari_lookup(ari)

gett = 'gettysburg_address.txt'
liz = 'f_lizst_let.txt'
holmes = 's_holmes.txt'
whit = 'w_whit_leaves.txt'

get_ari_info(gett)
get_ari_info(liz)
get_ari_info(holmes)
get_ari_info(whit)

