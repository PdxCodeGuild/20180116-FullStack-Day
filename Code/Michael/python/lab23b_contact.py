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
    return address_book


def create():
    answer = 'yes'
    while answer == 'yes':
        input_contact = []

        with open('contacts_csv.csv', 'a') as file:
            address_book = csv.writer(file)
            input_contact.append(input(f'Enter new contact name: \n> '))
            input_contact.append(input(f'enter new contact favorite fruit: \n> '))
            input_contact.append(input(f'Enter new contact favorite color: \n> '))
            address_book.writerow(input_contact)
        answer = input('would you like to create another contact?')
        return address_book


def retrieve(address_book):

    retrieve = input('Enter a name to retrieve their information:')

    for i in range(len(address_book)):
        if retrieve in address_book[i]['name']:
            print(f'You entered {retrieve}.')
            print(f"Their favorite fruit is {address_book[i]['favorite fruit']} and their favorite color is {address_book[i]['favorite color']}.")


def update(address_book):

    update_name = input('Whose information would you like to update? ')
    update_key = input('Which key would you like to change? ')
    update_value = input('What is the new value? ')

    for i in range(len(address_book)):
        if update_name in address_book[i]['name']:
            address_book[i][update_key] = update_value
            print(f'You entered {update_name}.')
            print(f'Their {update_key} is now {update_value}.')


def delete(address_book):
    del_name = input('Whose information would you like to delete?')

    for i in range(len(address_book) - 1):
        if del_name in address_book[i]['name']:
            del address_book[i]
            print(f'You have deleted {del_name} from the contacts list forever.')

    print(address_book)


def main():
    print('''
    What would you like to do? Select one.
    1. Read the current contacts
    2. Create a contact
    3. Retrieve a contact
    4. Update a contact
    5. Delete a contact
    6. Exit
    ''')

    addess_book = read()

    while True:
        option = input('Which operation would you like to perform?\n> ')

        if option == '1':
            print(addess_book)

        elif option == '2':
            create()

        elif option == '3':
            retrieve(addess_book)

        elif option == '4':
            update(addess_book)

        elif option == '5':
            delete(addess_book)

        elif option == '6':
            print('Exit')
            exit(0)

        else:
            print('Please type a valid response')


main()

