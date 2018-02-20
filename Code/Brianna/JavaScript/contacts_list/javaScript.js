






////// The Python version of some things  ///////

/*# Make a list for the dictionaries to go
contacts_dictionary_list = []
# Take off the header
header = lines.pop(0)
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

print(contacts_dictionary_list)

enter_new = True
while enter_new:
    new_contact = {}
    new_contact[header[0]] = input(f"Please enter new contact {header[0]}. \n:")
    new_contact[header[1]] = input(f"Please enter new contact {header[1]}. \n:")
    new_contact[header[2]] = input(f"Please enter new contact {header[2]}. \n:")
    contacts_dictionary_list.append(new_contact)
    done = input("Would you like to add another contact? y or n?\n:")
    if done == 'n':
        enter_new = False

print(contacts_dictionary_list)

retrieve_contact = input("Would you like to retrieve a contact? y or n?\n:")

if retrieve_contact == 'y':
    contact_name = input("Who's information would you like to retrieve? Please enter a name.\n:")
    # The segment below is not running correctly. Look up how to retrieve information using values to find other values under a key.
    if contact_name in range(contacts_dictionary_list[header[0]][contact_name]):
        print(f"{contacts_dictionary_list[i][header[0]]}'s favorite fruit is {contacts_dictionary_list[i][header[1]]} and their favorite color is {contacts_dictionary_list[i][header[2]]}.")
    else:
        print("I'm sorry. I could not find " + contact_name + ".")
*/
