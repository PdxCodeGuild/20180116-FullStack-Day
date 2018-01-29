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

def add_new_contact(contacts_file):
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
    enter_new = True
    while enter_new:
        input_contact = {}
        input_contact[header[0]] = input(f"Please enter new contact {header[0]}. \n:")
        input_contact[header[1]] = input(f"Please enter new contact {header[1]}. \n:")
        input_contact[header[2]] = input(f"Please enter new contact {header[2]}. \n:")
        contacts_dictionary_list.append(input_contact)
        done = input("Would you like to add another contact? y or n?\n:")
        if done == 'n':
            enter_new = False
    return contacts_dictionary_list


retrieve_contact = input("Would you like to retrieve a contact? y or n?\n:")

if retrieve_contact == 'y':
    contact_name = input("Who's information would you like to retrieve? Please enter a name.\n:")
print(contacts_dictionary_list[header[0]:contact_name])



    #if contact_name in contacts_dictionary_list:
    #    contact_output = contacts_dictionary_list.get(header[0]: contact_name, header[1]: , header[2] :)
#print(contact_output)






'''
'''
Implement a CRUD REPL

 Retrieve a record: ask the user for the 
contact's name, find the user with the given name, and display their 
information Update a record: ask the user for the contact's name, 
then for which attribute of the user they'd like to update and the value
 of the attribute they'd like to set. Delete a record: ask the user for 
 the contact's name, remove the contact with the given name from the contact list.
 '''