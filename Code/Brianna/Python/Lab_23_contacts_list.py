with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)


# split into list of dictionaries

contacts_dictionary_list = []

# split list by commas?
header = lines.pop(0)
print(header)

header = header.split(',')
print(header)


contact_values = [contact.split(',') for contact in lines]

print(contact_values)

#contact_dictionary = {header[:i]: contact_values[:i] for i in contact_values}
#print(contact_dictionary)

for contact in range(len(contact_values)):
    new_contact = {}
    new_contact[header[0]] = contact_values[contact][0]
    new_contact[header[1]] = contact_values[contact][1]
    new_contact[header[2]] = contact_values[contact][2]
    contacts_dictionary_list.append(new_contact)

print(contacts_dictionary_list)

