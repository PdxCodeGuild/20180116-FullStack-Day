import string
import re
import math

valid_letters = string.ascii_lowercase

path = input("Enter the path of the book to open (files/name_of_book.txt): ")
novel = input("What is the name of the book? ")


def calc():
    with open(path, 'r') as f:
        contents = f.read().lower()
        new_contents = contents.replace('\n', ' ')
        sentence = re.split("[.!?]", new_contents)
        stripped = contents.translate(string.punctuation)
        # use re instead?
        for char in stripped:
            if char not in valid_letters:
                stripped = stripped.replace(char, ' ')
        # use re instead?
        word = stripped.split(' ')
        while '' in word:
            word.remove('')
        chars = len(stripped) - stripped.count(' ')
        return chars, word, sentence


def ari(c, w, s):
    result = 4.71 * (c / w) + 0.5 * (w / s) - 21.43
    result = math.ceil(result)
    return result


characters, words, sentences = calc()


character_count = float(characters)
word_count = float(len(words))
sentence_count = float(len(sentences))

print(f"{novel} has {character_count} characters.")
print(f"{novel} has {word_count} words.")
print(f"{novel} has {sentence_count} sentences.\n")


ari_score = ari(character_count, word_count, sentence_count)

if ari_score > 14:
    ari_score = 14

ari_scale = {
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

print('-' * 20)
print(f"The ARI score for {novel} is: {ari_score}")
print(f"This corresponds to a {ari_scale[ari_score]['grade_level']} level of difficulty")
print(f"That is suitable for an average person {ari_scale[ari_score]['ages']} years old.")
print('-' * 20)
