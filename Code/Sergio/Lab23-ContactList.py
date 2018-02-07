"""
Lab 23: Contact List v2
"""

# global string so you don't have to change it in every function in v2
opencontacts = 'contacts.csv'

# opens contacts with 'r' = read attribute
with open(opencontacts, 'r') as file:
    lines = file.read().split('\n')  # reads file and splits to new line, but not really splitting
    # count words/sentences/characters

    contacts = []  # empty contact list
    # append contact list of lines index and split by commas,
    for i in range(len(lines)):
        contacts.append(lines[i].split(','))
    contact_dictionary = {}  # empty dict
    contact_list = []  # dictionaries within lists
    for i in range(1, len(contacts) - 1):  # gets length of items, 1 excludes the headers
        # arranged as keys and values
        contact_dictionary = {
            contacts[0][0]: contacts[i][0],
            contacts[0][1]: contacts[i][1],
            contacts[0][2]: contacts[i][2],
        }
        contact_list.append(contact_dictionary)  # contact list gets appended to individual dictionaries

"""Begin CRUD REPL: Create, retreive, update, delete"""
"""" USE contact_list FROM NOW ON """


def create():
    new_user_dict = {}  # empty dictionary for new user entries
    new_name = input('New name: ')
    new_fruit = input('New fruit: ')
    new_color = input('New color: ')
    new_user_dict['name'] = new_name
    new_user_dict['favorite fruit'] = new_fruit
    new_user_dict['favorite color'] = new_color
    contact_list.append(new_user_dict)


create()


def retrieve():
    retrieve_user = input('Who\'s name would you like to retrieve? ')
    for person in contact_list:
        if retrieve_user == person['name']:
            print(person)


retrieve()


def update():
    update_user = input('Who\'s name would you like to update? ')
    for person in contact_list:
        if update_user == person['name']:
            print(person)
            new_fruit = input('New fruit: ')
            new_color = input('New color: ')
            person['favorite fruit'] = new_fruit
            person['favorite color'] = new_color
            print(contact_list)
            break  # test


update()


def delete():
    delete_user = input('Who\'s name would you like to delete from the list? ')
    for person in contact_list:
        if person['name'] == delete_user:
            del person['name']
    print(contact_list)


delete()
