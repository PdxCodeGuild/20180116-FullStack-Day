#Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together,
#and go over how to load that file.
#Headers might consist of name, favorite fruit, favorite color. Open the CSV,
#convert the lines of text into a list of dictionaries, one dictionary for each user.
#The text in the header represents the keys, the text

import csv

def load_contacts():
    with open('contacts_csv.csv', 'r') as file:
        lines = file.read().split('\n')
        print(lines)
    contacts = []
    headers = lines.pop(0)
    headers = headers.split(',')
    for line in lines:
        line = line.split(',')
        new_dict = {}
        for i in range(len(line)):
            new_dict[headers[i]] = line[i]
        contacts.append(new_dict)
    print(contacts)
    return contacts

'''Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
'''


def create(contacts):

    add_name = input('What contact name?\n:')
    add_fruit = input('What fruit?\n:')
    add_color = input('What color?')
    with open('contacts_new.csv', 'w') as file:
        lines = csv.writer(file)
        lines.writerow(contacts[0].keys())

    contacts.append({'name': add_name, 'favorite fruit': add_fruit, 'favorite color': add_color})

    with open('contacts_new.csv', 'a') as file:
        lines = csv.writer(file)
        lines.writerow() #loop this for values in each line
        for contact in contacts:
            lines.writerow(contact)


def retrieve(address_book):

    retrieve_name = input('name lookup')
    for name in address_book:
        if retrieve_name in name.values():
            print(name)


def update(address_book):

    with open('contacts_new.csv', 'w') as file:
        lines = file.write()
    retrieve_name = input('name of contact to change: ')
    update_name = input('contact\'s new name: ')
    for contact in address_book:
        if contact['name'] == retrieve_name:
            contact['name'] = update_name
            break


def delete(address_book):
    with open('contacts_new.csv', 'r') as file:
        lines = file.write()
    delete_name = input('Which name would you like to delete?')
    for contact in address_book:
        if contact['name'] == delete_name:
            address_book.remove(contact)
            break

#When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup
#  contacts.csv because you likely won't write it correctly the first time.
#def main(address_book):




address_book = load_contacts()
create(address_book)

print(address_book)