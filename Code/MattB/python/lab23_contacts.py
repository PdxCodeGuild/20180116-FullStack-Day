def new_contact():
    n_contact = {}
    for key in range(len(keys)):
        n_contact[keys[key]] = input(f'{keys[key]}: \n> ')
        contacts.append(n_contact)
    print('Added new contact, would you like to view your updated list?')
    command2 = input('\'yes\' or \'no\':\n> ')
    if command2 == 'yes':
            print('-' * 15)
            print(contacts)
    elif command2 == 'no':
            exit()
    return contacts


def update_contact(*a):
    for cates in range(len(a)):
        print(a[cates])
    update = input('Which category would you like to update?\n> ')
    for cates in range(len(a)):
        if update in a[cates]:
            new = input(f'Enter new {a[cates]}.\n> ')
            a[cates][update] = new
            print(a[cates])
            print('-' *15)
            return a[cates]
        else:
            yesorno = input('That category does not exist, would you like to add it to the contact?\n> ')
            if yesorno == 'yes':
                newest = input(f'What is your {update}?\n> ')
                a[cates][update] = newest
                print(a[cates])
                print('-' * 15)
                return a[cates]

def retrieve_contact(check):
    for names in range(len(contacts)):
        if check.lower() in str(contacts[names]).lower():
            x = contacts[names]
            print(contacts[names])
            print('-' * 15)
            command5 = input('Would you like to \'update\' or \'delete\' this contact?\n> ')
            if command5 == 'update':
                update_contact(x)
                return x
            elif command5 == 'delete':
                contacts.remove(x)
                print(contacts)
                return contacts
            else:
                return x
    y_n = input('That contact does not exist, would you like to make a new one?\n> ')
    if y_n == 'yes':
        new_contact()
    else:
        exit()


with open('contacts_csv.csv', 'r') as file:
    lines = file.read().split('\n')

    contacts = []
    for i in range(1, len(lines)):
        contact = {}
        keys = lines[0].split(',')
        cats = lines[i].split(',')
        for key in range(len(keys)):
            contact[keys[key]] = cats[key]
        contacts.append(contact)

    #print(contacts[5])


    print('Hello, welcome to Contacts.')
    print('What would you like to do: "NEW" or "RETRIEVE" contact?: ')
    command = input('> ')
    print('-' * 15)

    # Code for adding a new contact to the list.
    if command == 'NEW':
        new_contact()

    # Code for retrieving a contact by name
    elif command == 'RETRIEVE':
        name = input('type the name of the contact you wish to view.\n> ')
        retrieve_contact(name)

