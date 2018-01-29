"""
Lab 23
Contact list
"""

with open('files/contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    items = []
    for i in range(len(lines)):
        items.append(lines[i].split(','))
    contact_dict = {}
    contact_list = []
    for i in range(1, len(items)):
        contact_dict = {items[0][0]: items[i][0], items[0][1]: items[i][1], items[0][2]: items[i][2]}
        contact_list.append(contact_dict)

print(contact_list)

