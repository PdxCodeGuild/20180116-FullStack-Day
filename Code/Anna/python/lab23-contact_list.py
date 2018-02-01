"""
Lab 23
Contact list
"""

from twilio.rest import Client

with open('files/contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    items = []
    for i in range(len(lines)):
        items.append(lines[i].split(','))
    contact_dict = {}
    contact_list = []
    for i in range(1, len(items)):
        contact_dict = {items[0][0]: items[i][0], items[0][1]: items[i][1], items[0][2]: items[i][2]}
        contact_list.append(contact_dict)

print(contact_list)


# Version 2.5 - using classes and methods FTW!


class ContactManager:
    """This does things to the existing contact list"""

    def __init__(self, contact_list):
        """Initialize contact list"""
        self.contact_list = contact_list

    def add_contact(self):
        """Create a record"""
        print("\nLet's add some contacts!")
        name = input("Enter your contact's name: ")
        fruit = input("Enter their favorite fruit: ")
        color = input("Enter their favorite color: ")

        contact_list.append({'name': name, 'favorite fruit': fruit, 'favorite color': color})

        print(contact_list)

    def retrieve_contact(self):
        """Retrieve a record"""
        print("\nLet's retrieve a contact.")
        retrieve = input("Enter a name to get their information: ")

        for i in range(len(contact_list)):
            if retrieve in contact_list[i]['name']:
                print(f"You entered {retrieve}.")
                print(f"Their favorite fruit is {contact_list[i]['favorite fruit']} and their favorite color is {contact_list[i]['favorite color']}.")

    def update_contact(self):
        """Update a record"""
        print("\nLet's update a contact's information.")
        update_name = input("Whose information would you like to update? ")
        update_key = input("Which key would you like to change? ")
        update_value = input("What is the new value? ")

        for i in range(len(contact_list)):
            if update_name in contact_list[i]['name']:
                contact_list[i][update_key] = update_value
                print(f"You entered {update_name}.")
                print(f"Their {update_key} is now {update_value}.")

        print(contact_list)

    def delete_contact(self):
        """Delete a record"""
        print("\nOh no, it's time to delete someone from our contacts list!")
        del_name = input("Whose information would you like to delete? ")

        for i in range(len(contact_list) - 1):
            if del_name in contact_list[i]['name']:
                del contact_list[i]
                print(f"You have deleted {del_name} from the contacts list forever. Hope you're happy with yourself.")

        print(contact_list)


def user_input():
    print("Welcome to the Contact List Manager. Would you like to add, retrieve, update, or delete a contact?")
    inp = input("> ")
    return inp


def contact_manager(choice):
    if choice == 'add':
        my_contacts.add_contact()
        cont = input("Would you like to perform another operation? y/n ")
        if cont == 'y':
            choice = user_input()
            contact_manager(choice)
        else:
            print("Goodbye!")
    elif choice == 'retrieve':
        my_contacts.retrieve_contact()
        cont = input("Would you like to perform another operation? y/n ")
        if cont == 'y':
            choice = user_input()
            contact_manager(choice)
        else:
            print("Goodbye!")
    elif choice == 'update':
        my_contacts.update_contact()
        cont = input("Would you like to perform another operation? y/n ")
        if cont == 'y':
            choice = user_input()
            contact_manager(choice)
        else:
            print("Goodbye!")
    elif choice == 'delete':
        my_contacts.delete_contact()
        cont = input("Would you like to perform another operation? y/n ")
        if cont == 'y':
            choice = user_input()
            contact_manager(choice)
        else:
            print("Goodbye!")
    else:
        print("That is not a valid option.")
        cont = input("Would you like to perform another operation? y/n ")
        if cont == 'y':
            choice = user_input()
            contact_manager(choice)
        else:
            print("Goodbye!")


my_contacts = ContactManager(contact_list)
choice = user_input()
contact_manager(choice)


# Version 3

with open('files/contacts.csv', 'w') as file:
    for i in range(len(contact_list)):
        file.write(contact_list[i]['name'] + ',' + contact_list[i]['favorite fruit'] + ',' + contact_list[i]['favorite color'] + "\n")


# Version 4

for i in range(len(contact_list)):
    contact_list[i]['phone number'] = "503-100-2000"

print(contact_list)

# account_sid = ""
# auth_token = ""
# client = Client(account_sid, auth_token)
#
# message = client.api.account.messages.create(to="<whatever you like>",
#                                              from_="+19718033720",
#                                              body="Hello there!")
#
# print(message.sid)