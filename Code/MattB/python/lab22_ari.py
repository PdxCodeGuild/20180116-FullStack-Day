remove = ['\'', '*', ',', '?', '!', ':', ';', '\"', '[', ']', '_', '-', '(', ')']

def avg(a_list):
    count = 0
    for a in range(len(a_list)):
        count += len(a_list[a])
    avg_of = count / len(a_list)
    return avg_of

with open('book.txt', 'r', encoding="utf8") as book:
    book = book.read()
    book = book.lower()
    book = book.replace('\n', ' ')
    book = book.replace('mr.', 'mr')
    book = book.replace('mrs.', 'mrs')
    sentence = book.split('.')
    words = book.split(' ')

    for i in range(len(sentence)):
        for j in range(len(remove)):
            if remove[j] in sentence[i]:
                sentence[i] = sentence[i].replace(remove[j], '')

    remove.append('.')
    for m in range(len(words)):
        for n in range(len(remove)):
            if remove[n] in words[m]:
                words[m] = words[m].replace(remove[n], '')

    count2 = 0
    for b in range(len(sentence)):
        count2 += sentence[b].count(' ') - 1

    avg2 = count2 / len(sentence)

    ari = int(4.71 * avg(words) + 0.5 * avg2 - 21.43)

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

print(f'The ARI for the text is {ari}.\n'
      f'This corresponds to a {ari_scale[ari]["grade_level"]} reading level \n'
      f'that is suitable for an average person {ari_scale[ari]["ages"]} years old.')

