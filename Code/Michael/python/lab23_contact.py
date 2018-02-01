import csv

with open('contacts_csv.csv', 'r') as file:
    lines = file.read().split('\n')

    address_book = []

    header = lines.pop(0)
    header = header.split(',')

for contacts in lines:
    contact_val = contacts.split(',')

    my_dict = {}

    for i in range(len(contact_val)):
        my_dict[header[i]] = contact_val[i]

    address_book.append(my_dict)

print(address_book)

