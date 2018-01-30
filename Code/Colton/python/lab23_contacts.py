dictionary = []
with open('contacts_csv.csv', 'r') as file:
    lines = file.read().split('\n')
    i = 0
    while i < len(lines):
        dictionary.append(lines[i:i + 1])
        i += 1
    dictionary_key = dictionary.pop(0)

print(dictionary_key)
print(dictionary)

