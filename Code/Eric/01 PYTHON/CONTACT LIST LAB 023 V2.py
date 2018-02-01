# VERSION 2: NOW WITH A CRUD REPL FEATURE!
"""Implement a CRUD REPL

1- Create a record: ask the user for each attribute,
2- add a new contact to your contact list with the attributes that the user entered.
3- Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
4- Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
5- Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list."""

# CONTACT LIST V1
with open('contacts_csv.csv', 'r') as file:
	lines = file.read().lower().split('\n')

contact_list = []

for l in lines[1:]:
	contacts = {}
	l = l.split(',')
	contacts['name'] = l[0]
	contacts['fav_fruit'] = l[1]
	contacts['fav_color'] = l[2]
	contact_list.append(contacts)


# CREATE NEW CONTACT
def new_contact():
	print('\nlet\'s add a new contact to our list!\n')

	user_name = ''
	user_fruit = ''
	user_color = ''

	while user_name == '':
		user_name = input('what is the contact name?\n:')
	while user_fruit == '':
		user_fruit = input('ok! now what is the contact\'s favorite fruit?\n:')
	while user_color == '':
		user_color = input('great! now what is the contact\'s favorite color?\n:')

	user_contacts = {'name': user_name, 'fav_fruit': user_fruit, 'fav_color': user_color}

	contact_list.append(user_contacts)
	contact_num = 0
	for c in contact_list:
		contact_num += 1
		print(f'CONTACT {contact_num}:\n{c}\n')
	return contact_list


# CONTINUE ADDING NEW CONTACTS
def another_contact():
	another_contact_ = ''
	another_contact_ = another_contact_.lower()
	print('\nwould you like to add a new contact?\n')
	while True:
		another_contact_ = input('type "yes" or "no"\n:')
		if another_contact_ == 'yes':
			return new_contact()
		elif another_contact_ == 'no':
			break


# RETRIEVE A CONTACT
# def lookup(contact_list):
# 	user_search = input('\ntype the name of the contact you would like to search for\n:')
# 	user_search = user_search.lower()
# 	for dictionary in contact_list:
# 		for key in dictionary:
# 			if user_search == contact_list[dictionary][key]:
# #
#
#
#
#
#
# lookup(contact_list)

while True:
	another_contact()
