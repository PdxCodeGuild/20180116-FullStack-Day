# Let's build a program to manage a list of contacts.
# To start, we'll build a CSV ('comma separated values')
# together, and go over how to load that file.
# Headers might consist of name, favorite fruit, favorite color. Open the CSV,
# convert the lines of text into a list of dictionaries, one dictionary for each user.
# The text in the header represents the keys, the text in the other lines represent the values.
#
#
# with open('contacts.csv', 'r') as file:
#     lines = file.read().split('\n')
#     print(lines)
# Once you've processed the file, your list of contacts will look something like this...
#
# contacts = [
#     {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
# #
# Implement a CRUD REPL
#
# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.


default_path = f'/Users/magdalene/PyFiles/CodeGuild/2018coursework/Code/Maggie/resources/'
filename = 'contacts.csv'

def load_text():
    ascii_art = '''   (\_/)
   'o.o'
  =(_ _)=
     U \n'''
    project_name = 'Contacts list v0.0 - Maggie Geise, 2018\n'
    print(ascii_art, project_name)

def import_file(file_name):
    with open(default_path + 'contacts.csv', 'r') as f:
        lines = f.read().split('\n')
    lines_list = []
    for comma_str in lines:
        lines_list.append(comma_str.split(','))
    print('...Contacts imported.')
    return lines_list

def convert_to_contacts_list(imported_list):
    contacts_list = []
    for i in range(1, len(imported_list)):
        d = {}
        for j in range(len(imported_list[i])):
            d.update({imported_list[0][j]: imported_list[i][j]})
        contacts_list.append(d)
    print('...list loaded.')
    return contacts_list

def append_contacts(contacts_list):  # add a new entry to the contact list
    print('Add a new value to the contact list.')
    new_name = input('Contact name: ')
    new_fruit = input(f'{new_name}\'s favorite fruit: ')
    new_color = input(f'{new_name}\'s favorite color: ')
    new_record = {'name' : new_name, 'favorite fruit' : new_fruit, 'favorite color ' : new_color }
    contacts_list.append(new_record)
    print(f'...{new_record} appended to contact list.')
    return contacts_list

def retrieve_record_index(contacts_list):  # pull up a record by name, display information
    print('Please enter a name to look up a record.')
    contact_name = input('Contact name: ')
    for index in range(len(contacts_list)):
        if contacts_list[index]['name'] == contact_name:
            return index
        else:
            print('Sorry. That entry does not appear to be in the contact list.')
    print('...record retrieved')

def update_record(contacts_list, index):
    key_search_term = input('Your choice: ')
    replacement_value = input('Your choice: ')
    for n, key in enumerate(contacts_list[index].keys):
        print(f'{n}. {key}')
        if key == key_search_term:
            contacts_list[key] = replacement_value
    return contacts_list

def delete_record(contact_list, index):
    contact_list.pop(index)

def print_record(contacts_list, index):
    record_disp = '\n'.join(f'{key}: {val}' for key, val in contacts_list[index].items())
    print(record_disp)

# def option_loop(contact_list):
#     c_l = contact_list
#     rec_ind = retrieve_record_index(c_l)
#     function_sel = [append_contacts(c_l), print_record(rec_ind), update_record(rec_ind), delete_record(rec_ind)
#                     ]
#     options = ['Create a new record', 'Retrieve an existing entry', 'Update an existing entry', 'delete a record']
#     print('User options: ', enumerate(options))
#     u_choice = input('Your choice')
#
#     try:
#         u_choice = funct_select[str(u_choice)[0]]
#         # break
#     except KeyError:
#         print('Invalid choice. Try again.')

def main():
    load_text()
    imported_list = import_file(filename)
    contacts_list = convert_to_contacts_list(imported_list)
    option_loop()


main()