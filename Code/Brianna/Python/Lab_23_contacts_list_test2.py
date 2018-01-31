with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)


# Work on splitting into list of dictionaries
def make_contact_dict(contacts_file):
    # Make a list for the dictionaries to go
    contacts_dictionary_list = []
    # Take off the header
    header = contacts_file.pop(0)
    # Split header by commas for use
    header = header.split(',')
    # Split contact values into a list
    contact_values = [contact.split(',') for contact in lines]
    for contact in range(len(contact_values)):
        new_contact = {}
        new_contact[header[0]] = contact_values[contact][0]
        new_contact[header[1]] = contact_values[contact][1]
        new_contact[header[2]] = contact_values[contact][2]
        contacts_dictionary_list.append(new_contact)
    return contacts_dictionary_list


contact_dictionary = make_contact_dict(lines)

print(contact_dictionary)


def add_new_contact(contact_dictionary):
    enter_new = True
    while enter_new:
        input_contact = {}
        input_contact['name'] = input(f"Please enter new contact name. \n:")
        input_contact['favorite fruit'] = input(f"Please enter new contact favorite fruit. \n:")
        input_contact['favorite color'] = input(f"Please enter new contact favorite color. \n:")
        contact_dictionary.append(input_contact)
        done = input("Would you like to add another contact? y or n?\n:")
        if done == 'n':
            enter_new = False
    return contact_dictionary


new_dictionary = add_new_contact(contact_dictionary)

print(new_dictionary)

'''
retrieve_contact = input("Would you like to retrieve a contact? y or n?\n:")

if retrieve_contact == 'y':
    contact_name = input("Who's information would you like to retrieve? Please enter a name.\n:")

for dictionary in new_dictionary: # looping through dictionaries in the list of dictionaries
    if dictionary['name'] == contact_name:  # Seeing if the key 'name' value matches the users input contact_name:
        print(dictionary) # just prints the dictionary. Should probably make it fancier. :-)
'''

# Making a function to find a key within a list of dictionaries and output info related to it.
def retrieve_info(list_name):
    key_name = input("What contact information would you like to retrieve? ie: name, favorite fruit, favorite color.\n")
    value_name = input("What is the value? For example, blue, or watermelon.\n")
    for dictionary in list_name:
        if dictionary[key_name] == value_name:
        return(dictionary)

user_dictionary = retrieve_info(new_dictionary)




'''

    #if contact_name in contacts_dictionary_list:
    #    contact_output = contacts_dictionary_list.get(header[0]: contact_name, header[1]: , header[2] :)
#print(contact_output)

# Remove an item from a list: list_name.remove('value')

'''

'''

for i in range(len(contact_list)):
    if retrieve in contact_list[i]['name']:
        print(f"You entered {retrieve}.")
        print(f"Their favorite fruit is {contact_list[i]['favorite fruit']} and their favorite color is {contact_list[i]['favorite color']}.")


Implement a CRUD REPL

 Retrieve a record: ask the user for the 
contact's name, find the user with the given name, and display their 
information Update a record: ask the user for the contact's name, 
then for which attribute of the user they'd like to update and the value
 of the attribute they'd like to set. Delete a record: ask the user for 
 the contact's name, remove the contact with the given name from the contact list.



 '''