def create():
    create = []
    create_name = input('What is the name you want to add?\n:')
    create_fruit = input('What is their favorite fruit?\n:')
    create_color = input('What is their favorite colot?\n:')
    create.append(create_name)
    create.append(create_fruit)
    create.append(create_color)  ####creates the new list for the contact
    for i in range(len(header)):
        key = header[i]
        value = create[i]
        contact_2[key] = value
    print(contacts)
    return create


def retrieve():
    retrieve = input("Which person would you like info about? Type done to exit\n:")
    for i in range(len(contacts)):
        if retrieve == contacts[i]['name']:
            print(contacts[i])
            break
        elif retrieve == 'done':
            break
        elif retrieve != contacts[i]['name']:
            print("Name not availible, try another name.")
            continue
    return retrieve


def update():
    update = input("Which user would you like to update?")
    for i in range(len(contacts)):
        if update == contacts[i]['name']:
            print(contacts[i])
    update_specs = input("What would you like to update?\n:Name, favorite fruit, or  favorite color\n:").lower()
    ################UPDATE NAME##################################
    if update_specs == 'name':
        new_name = input("Type a new name\n:")
        for i in range(len(contacts)):
            if update == contacts[i]['name']:
                contacts[i].update({'name': new_name})
                print(contacts)

            break

    ###############UPDATE FRUIT ###########################
    if update_specs == 'favorite fruit':
        new_fruit = input("Type a new fruit\n:")
        for i in range(len(contacts)):
            if update == contacts[i]['favorite fruit']:
                contacts[i].update({'name': new_fruit})
                print(contacts)

            break

    ###############UPDATE COLOR ###########################
    if update_specs == 'favorite color':
        new_color = input("Type a new color\n:")
        for i in range(len(contacts)):
            if update == contacts[i]['favorite color']:
                contacts[i].update({'favorite color': new_color})
                print(contacts)

            break
    return update()


def delete():
    delete = input("Which contact do you want to delete? Type done to exit.\n:")
    for i in range(len(contacts)):
        if delete == contacts[i]['name']:
            del (contacts[i])
            print(contacts)
            break
        if delete == 'done':
            break
    return delete()


###########################################################################
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
    for i in range(len(contacts)):
        print(contacts[i])
    crud = input(
        "Choose your option.\nCreate a new record\nRetrieve a new record\nUpdate a record\nDelete a record\n:::").lower()

    while crud not in options:
        crud = input(
            "Choose your option.\nCreate a new record\nRetrieve a new record\nUpdate a record\nDelete a record\n:::").lower()
    ######################CREATE#########################
    while crud in options:
        if crud == 'create':
            create()

        ######################RETRIEVE#################################
        elif crud == 'retrieve':
            retrieve()

        #####################UPDATE########################
        elif crud == 'update':
            update()
        ###################DELETE##########################
        elif crud == 'delete':
            delete()

# contacts = str(contacts)
#
# with open('contacts_csv.csv', 'w') as file:
#     file.write(contacts)