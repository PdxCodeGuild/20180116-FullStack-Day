import csv

def read():

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


def create():

    input_contact = []
    with open('contacts_csv.csv', 'a') as file:
        address_book = csv.writer(file)
        input_contact.append(input(f"Please enter new contact name: \n> "))
        input_contact.append(input(f"Please enter new contact favorite fruit: \n> "))
        input_contact.append(input(f"Please enter new contact favorite color: \n> "))
        address_book.writerow(input_contact)
        new_addresses = address_book

def retrieve():

    read()

read()

create()

retrieve()
