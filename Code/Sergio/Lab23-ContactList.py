"""
Lab 23: Contact List v1
"""

# global string so you don't have to change it in every function in v2
opencontacts = 'contacts.csv'

# opens contacts with 'r' = read attribute
with open(opencontacts, 'r') as file:
    lines = file.read().split('\n')  # reads file and splits to new line, but not really splitting
    # count words/sentences/characters

    contacts = [] # empty contact list
    # append contact list of lines index and split by commas,
    for i in range(len(lines)):
        contacts.append(lines[i].split(','))
    contact_dictionary = {}  # empty dict
    contact_list = []  # dictionaries within lists
    for i in range(1, len(contacts)):  # gets length of items, the "1" doesn't return the index of contacts
        # arranged as keys and values
        contact_dictionary = {
            contacts[0][0]: contacts[i][0],
            contacts[0][1]: contacts[i][1],
            contacts[0][2]: contacts[i][2],
        }
        contact_list.append(contact_dictionary)  # contact list gets appended to individual dictionaries

print(contact_list)
