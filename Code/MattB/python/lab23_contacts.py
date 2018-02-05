def new_contact():
    n_contact = {}
    for key in range(len(headers)):
        n_contact[headers[key]] = input(f'{headers[key]}: \n> ')
        contacts.append(n_contact)
    print('Added new contact, would you like to view your updated list?')
    command2 = input('\'yes\' or \'no\':\n> ')
    if command2 == 'yes':
        print('-' * 15)
        print(contacts)
        make_string(contacts)
    elif command2 == 'no':
        make_string(contacts)
    return contacts


def update_contact(*a):
    #print(a)
    print(list(a[0].keys()))
    update = input('Which category would you like to update?\n> ')
    for cates in range(len(a)):
        if update in a[cates]:
            new = input(f'Enter new {a[cates]}.\n> ')
            a[cates][update] = new
            print(a[cates])
            print('-' * 15)
        else:
            yesorno = input('That category does not exist, would you like to add it to the contact?\n> ')
            if yesorno == 'yes':
                newest = input(f'What is your {update}?\n> ')
                a[cates][update] = newest
                print(a[cates])
                print('-' * 15)
    make_string(contacts, a[cates])
    return contacts


def retrieve_contact(c_list):
    print(c_list)
    name = input('Type the name of the contact you wish to view.\n> ')
    for names in range(len(c_list)):
        if name.lower() in str(c_list[names]).lower():
            x = c_list[names]
            print(c_list[names])
            print('-' * 15)
            command5 = input('Would you like to \'update\' or \'delete\' this contact?\n> ')
            if command5 == 'update':
                update_contact(x)
                return x
            elif command5 == 'delete':
                c_list.remove(x)
                print(c_list)
                make_string(c_list, c_list[0])
                return c_list
            else:
                return x
    y_n = input('That contact does not exist, would you like to make a new one?\n> ')
    if y_n == 'yes':
        new_contact()
    else:
        exit()


def make_string(b, c):
    save = input('Would you like to save your updated list?\n> ')
    if save.lower() == 'yes':
        final = ','.join(c.keys())
        for f_lines in range(len(b)):
            adding = ','.join(list(b[f_lines].values()))
            final = final + '\n' + adding
        print(final)
        with open('csv_test.csv', 'w') as finish:
            finish.write(final)
            finish.close()
        return b
    else:
        exit()


with open('csv_test.csv', 'r') as file:
    lines = file.read().split('\n')

headers = lines[0].split(',')
contacts = []
for i in range(1, len(lines)):
    contact = {}
    cats = lines[i].split(',')
    for key in range(len(headers)):
        contact[headers[key]] = cats[key]
    contacts.append(contact)

# print(contacts[5])
print('Hello, welcome to Contacts.')
print('What would you like to do: "NEW" or "RETRIEVE" contact?: ')
command = input('> ')
print('-' * 15)

# Code for adding a new contact to the list.
if command == 'NEW':
    new_contact()

# Code for retrieving a contact by name
elif command == 'RETRIEVE':
    retrieve_contact(contacts)
