contacts = []
with open('contacts_csv.csv', 'r') as file:
    lines = file.read().split('\n')
    i = 0
    while i < len(lines):
        contacts.append(lines[i].split(','))
        i += 1
    header = contacts.pop(0)

    contacts_2 = []
    for contact in contacts:
        contact_2 = {}
        for i in range(len(header)):
            key = header[i]
            value = contact[i]
            contact_2[key] = value
        contacts_2.append(contact_2)
    contacts = contacts_2
    options = ('create', 'retrieve', 'update', 'delete')
    crud = input("Choose your option.\nCreate a new record\nRetrieve a new record\nUpdate a record\nDelete a record\n:::").lower()

    while crud not in options:
        crud = input("Choose your option.\nCreate a new record\nRetrieve a new record\nUpdate a record\nDelete a record\n:::").lower()

    while crud in options:
        if crud == 'create':
            create = []
            create_name = input('What is the name you want to add?\n:')
            create_fruit = input('What is their favorite fruit?\n:')
            create_color = input('What is their favorite colot?\n:')
            create.append(create_name)
            create.append(create_fruit)
            create.append(create_color)####creates the new list for the contact
            for i in range(len(header)):
                key = header[i]
                value = create[i]
                contact_2[key] = value
            print(contacts)
            again = input('Add another?').lower()
            if again == 'yes':
                continue
            if again != 'yes':
                break


        elif crud == 'retrieve':###still printing name not availible, cant use elif
            fetch = input("Which person would you like info about?\n:")
            for i in range(len(contacts)):
                if fetch == contacts[i]['name']:
                    print(contacts[i])
            if fetch != contacts[i]['name']:
                    print("Name not availible, try another name.")
                    continue



        # if crud == 'update':
        #     update = input("What would you like to update?\n:Name, fruit, or color?").lower()
        #     if update == 'name':
        #         pass
        #
        #     if update == 'fruit':
        #         pass
        #
        #     if update == 'color':
        #         pass

        elif crud == 'delete':###deletes name but then says index out of range
             delete = input("Which contact do you want to delete?")
             for i in range(len(contacts)):
                 if delete == contacts[i]['name']:
                     del(contacts[i])
                     print(contacts)
             if delete != contacts[i]['name']:
                 print("Name not availible, try another name.")


