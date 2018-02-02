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
    return address_book


def write(address_book):
    with open('contacts_csv.csv', 'w') as file:
        ...


def create():
    answer = 'yes'
    while answer == 'yes':
        input_contact = []

        # add a new contact to your list of contacts
        # call write(address_book)

        with open('contacts_csv.csv', 'a') as file:
            address_book = csv.writer(file)
            input_contact.append(input(f"Enter new contact name: \n> "))
            input_contact.append(input(f"enter new contact favorite fruit: \n> "))
            input_contact.append(input(f"Enter new contact favorite color: \n> "))
            address_book.writerow(input_contact)
        answer = input("would you like to create another contact?")


def retrieve():
    key_name = input("What would you like to retrieve? \n> ")
    value_name = input("What is the value? \n> ")


def update():
    updater = read()
    new_dict = {}
    with open('contacts_csv.csv', 'w') as file:
        address_book = csv.writer(file)
        address_book.writerow(updater[0].keys())
    with open('contacts_csv.csv', 'a') as file:
        address_book = csv.writer(file)
        name = input(f"Name to update\n> ")
        for dict_line in range(address_book):

            new_dict =

        name = input(f"Value to update?\n> ")

        # if address_book == name:
        #     # address_book.writerow(update)
        #
        #     key_value = input(f"What else would you like to update? \n> ")
        #
        # if address_book == value:
        #     # address_book.writerow(update)

    while True:
        answer = input("would you like to update another contact?")
        if answer == 'yes':
            update()
            break
        elif answer ==  'no':
            break





def main():
    print('''
    What would you like to do? Select one.
    1. Read the current contacts
    2. Create a contact
    3. Retrieve a contact
    4. Update a contact
    5. Exit
    ''')

    addess_book = read()

    while True:
        option = input('Which operation would you like to perform?\n> ')

        if option == '1':
            print(addess_book)

        elif option == '2':
            create()

        elif option == '3':
            retrieve()

        elif option == '4':
            update()

        elif option == '5':
            print('Exit')
            exit(0)

        else:
            print('Please type a valid response')

    write(addess_book)

main()

