import csv


def read():
    # open the file with the csv module and then read the opened file and split the line breaks and assign it to lines.
    with open('contacts_csv.csv', 'r') as file:
        lines = file.read().split('\n')
        # we create and empty list where the file contents will be appended to.
        address_book = []
        # popping the header file we will hold onto its contents as the variable header.
        header = lines.pop(0)
        # the header is then split at the comma
        header = header.split(',')
        # the for loop is to iterate over the lines to split contacts at the comma and assign its contents into the variable contact_val
        for contacts in lines:
            contact_val = contacts.split(',')
            # an empty dictionay is created to hold the contact_val contents we iterate over in the next following for loop.
            my_dict = {}
            for i in range(len(contact_val)):
                # the contents of each index of control_val is passed into its respective header column and passed to my_dict.
                my_dict[header[i]] = contact_val[i]
                # my_dict is then appended to the empty list address_book
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
        answer = input('would you like to create another contact? Yes or no \n> ')
        return address_book


def retrieve(address_book):

    retrieve = input('Enter a name to retrieve their information:\n> ')

    for i in range(len(address_book)):
        if retrieve in address_book[i]['name']:
            print(f'You entered {retrieve}.')
            print(f"Their favorite fruit is {address_book[i]['favorite fruit']} and their favorite color is {address_book[i]['favorite color']}.")


def update(address_book):

    update_name = input('Whose information would you like to update?\n> ')
    update_key = input('Which key would you like to change?\n> ')
    update_value = input('What is the new value?\n> ')

    for i in range(len(address_book)):
        if update_name in address_book[i]['name']:
            address_book[i][update_key] = update_value
            print(f'You entered {update_name}.')
            print(f'Their {update_key} is now {update_value}.')


def delete(address_book):
    del_name = input('Whose information would you like to delete?\n> ')

    for i in range(len(address_book) - 1):
        if del_name in address_book[i]['name']:
            del address_book[i]
            print(f'You have deleted {del_name} from your contacts list.')

    print(address_book)


def main():
    '''
    main is the control mechanism where functions are called on to execute its sub-operations. The while loop keeps executing until option 6 is selcted and then exit is called to quit.
    '''
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

