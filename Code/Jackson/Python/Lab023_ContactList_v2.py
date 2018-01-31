"""
Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the
user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their
information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and
the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
"""

#read CSV file
with open('contacts_csv.csv', 'r') as file:
    lines = file.read().split('\n')

#hardcode the key names from the header
header_name = 'name'
header_favfruit = 'favorite fruit'
header_favcolor = 'favorite color'
location = 0

contacts = []
# create lists for each data point in line and use to create dictionary
for i in range(1, len(lines)):
    cells = lines[i].split(',')
    #print(cells) #test
    dictionary = {header_name:cells[0], header_favfruit:cells[1], header_favcolor:cells[2]}
    contacts.append(dictionary) #add dictionary to the list


#can put that in a function for each of the create,
def create(name, fruit, color):
    dictionary = {header_name: name, header_favfruit: fruit, header_favcolor: color}
    contacts.append(dictionary)
    return contacts


def retrieve(name):
    #search the entire list for the dictionary at 'key' of 'header_name' containing that name
    for i in range(len(contacts)):
        if name.lower() == contacts[i][header_name].lower():
            favfruit = contacts[i][header_favfruit]
            favcolor = contacts[i][header_favcolor]
            return favfruit, favcolor  # tuple packing
    return None

def update(name,change_field, change_answer):
    for i in range(len(contacts)):
        if name.lower() == contacts[i][header_name].lower():
            print('check')
            location = i
            if change_field.lower() == header_favfruit:
                # print('changing fruit')
                contacts[i][header_favfruit] = change_answer
                # print(contacts[i][header_favfruit])
            if change_field.lower() == header_favcolor:
                # print('changing color')
                contacts[i][header_favcolor] = change_answer
            break

def delete(name):
    for i in range(len(contacts)):
        if contacts[i][header_name].lower() == name.lower():
            contacts.pop(i)
            break

#ask user, what would you like to do
userinput = input(f'what would you like to do? Create, Retrieve, Update, or Delete:').lower()

if userinput == 'create':
    name = input('what is the first name of the individual?: ')
    fruit = input('what is their favorite fruit?: ')
    color = input('what is their favorite color?: ')
    create(name, fruit, color)
    print(contacts)

elif userinput == 'retrieve':
    name = input('what is the name of the user that you would like to retrieve?: ').lower()
    favfruit, favcolor = retrieve(name)  # tuple unpacking
    print(favfruit)
    print(favcolor)

elif userinput == 'update':
    """ Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to 
    update and the value of the attribute they'd like to set. """
    name = input('what is the name of the user that you would like to update?: ')
    change_field = input('what attribute would you like to change? (favorite fruit or favorite color ')
    change_answer = input('what is the value of the attribute that you would like to set?:')
    update(name, change_field, change_answer)
    print(contacts[location])

elif userinput == 'delete':
    name = input('which name would you like to delete')
    delete(name)
    print(contacts)

else:
    print("I am sorry, I did not understand your command, please run again")

