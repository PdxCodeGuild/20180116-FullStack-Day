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


# Version 2

# Create a record

print("\nLet's add some contacts!")
name = input("Enter your contact's name: ")
fruit = input("Enter their favorite fruit: ")
color = input("Enter their favorite color: ")

contact_list.append({'name': name, 'favorite fruit': fruit, 'favorite color': color})

print(contact_list)

# Retrieve a record

print("\nSweet! Now let's retrieve a contact.")
retrieve = input("Enter a name to get their information: ")

for i in range(len(contact_list)):
    if retrieve in contact_list[i]['name']:
        print(f"You entered {retrieve}.")
        print(f"Their favorite fruit is {contact_list[i]['favorite fruit']} and their favorite color is {contact_list[i]['favorite color']}.")

# Update a record

print("\nOK, now let's update a contact's information.")
update_name = input("Whose information would you like to update? ")
update_key = input("Which key would you like to change? ")
update_value = input("What is the new value? ")

for i in range(len(contact_list)):
    if update_name in contact_list[i]['name']:
        contact_list[i][update_key] = update_value
        print(f"You entered {update_name}.")
        print(f"Their {update_key} is now {update_value}.")

print(contact_list)

# Delete a record

print("\nOh no, it's time to delete someone from our contacts list!")
del_name = input("Whose information would you like to delete? ")

for i in range(len(contact_list) - 1):
    if del_name in contact_list[i]['name']:
        del contact_list[i]
        print(f"You have deleted {del_name} from the contacts list forever. Hope you're happy with yourself.")

print(contact_list)


# Version 3

with open('files/contacts.csv', 'w') as file:
    for i in range(len(contact_list)):
        file.write(contact_list[i]['name'] + ',' + contact_list[i]['favorite fruit'] + ',' + contact_list[i]['favorite color'] + "\n")


