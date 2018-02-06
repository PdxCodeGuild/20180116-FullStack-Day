# VERSION 2: NOW WITH A CRUD REPL FEATURE AND A MAIN MENU <3<3<3 !!

# CONTACT LIST V1
with open('contacts_csv.csv', 'r') as file:
	lines = file.read().lower().split('\n')

contact_list = []

for line in lines[1:]:
	contacts = {}
	line = line.split(',')
	contacts['name'] = line[0]
	contacts['fav_fruit'] = line[1]
	contacts['fav_color'] = line[2]
	contact_list.append(contacts)


# VIEW CONTACT LIST
def view_contacts():
	contact_num = 0
	for contact in contact_list[0:]:
		contact_num += 1
		print(f'CONTACT {contact_num}:\n{contact}\n')
	return contact_list


# CREATE NEW CONTACT
def new_contact():
	print('\nADD NEW CONTACT: ')
	user_name = ''
	user_fruit = ''
	user_color = ''
	while user_name == '':
		user_name = input('\nwhat is the contact name?\n:')
	while user_fruit == '':
		user_fruit = input('ok! now what is the contact\'s favorite fruit?\n:')
	while user_color == '':
		user_color = input('great! now what is the contact\'s favorite color?\n:')
	user_contacts = {'name': user_name, 'fav_fruit': user_fruit, 'fav_color': user_color}
	contact_list.append(user_contacts)
	view_contacts()
	return another_contact()


# CONTINUE CREATING NEW CONTACTS
def another_contact():
	another_contact_ = ''
	print('\nwould you like to add another contact?\n')
	while True:
		another_contact_ = input('type "yes" to add or "no" to return to main menu\n:')
		another_contact_ = another_contact_.lower()
		if another_contact_ == 'yes':
			return new_contact()
		elif another_contact_ == 'no':
			main_menu()


# RETRIEVE A CONTACT
def lookup():
	print('\nSEARCH CONTACTS: ')
	user_search = input('\ntype the name or information of the contact you would like to search for\n:')
	user_search = user_search.lower()
	search_results = {}
	for dictionary in contact_list:
		for key, value in dictionary.items():
			if user_search in value:
				search_results = dictionary
				print(f'CONTACT FOUND:\n{search_results}\n')
				return lookup_another()
	if user_search not in contact_list:
		print('\nsorry! there is no matching contact in the directory\n')
	return lookup_another()


# CONTINUE RETRIEVING CONTACTS
def lookup_another():
	lookup_another_ = ''
	lookup_another_ = lookup_another_.lower()
	print('\nwould you like to search for another contact?\n')
	while True:
		lookup_another_ = input('type "yes" or "no"\n:')
		if lookup_another_ == 'yes':
			return lookup()
		elif lookup_another_ == 'no':
			main_menu()


# UPDATE A RECORD
def update():
	print('\nUPDATE CONTACT INFORMATION: ')
	while True:
		user_update_name = input('\ntype the name of the contact that you would like to update\n:')
		user_update_name = user_update_name.lower()
		search_results = {}
		for dictionary in contact_list:
			for key, value in dictionary.items():
				if user_update_name in value:
					search_results = dictionary
					print(f'CONTACT FOUND:\n{search_results}\n')
					print('is this the contact that you would like to update?\n')
					while True:
						user_update_confirm = input('type "yes" or "no"\n:')
						user_update_confirm = user_update_confirm.lower()
						user_update_final = ''
						if user_update_confirm == 'yes':
							print('ok! what information would you like to update?\n')
							while True:
								update_field = input('type the name of the field that you would like to'
								                     ' update\n:')
								update_field = update_field.lower()
								if update_field in dictionary.keys():
									user_update_a = input(f'ok! what would you like to change '
									                      f'{update_field} to?\n:')
									user_update_a = user_update_a.lower()
									dictionary[update_field] = user_update_a
									user_update_final = dictionary
									print(f'\nINFORMATION UPDATED!\nNEW INFO:\n{user_update_final}\n\n')
									view_contacts()
									return update_again()
								elif update_field not in dictionary.keys():
									print('\nsorry! there is no such field!')
						elif user_update_confirm == 'no':
							print('\nok! let\'s try again!')
							return update()
		if user_update_name not in value:
			print('\nsorry! there is no matching contact in the directory\n')
		return update_again()


# CONTINUE UPDATING RECORDS
def update_again():
	update_again_ = ''
	update_again_ = update_again_.lower()
	print('\nwould you like to make another update?\n')
	while True:
		update_again_ = input('type "yes" for another or "no" to return to the main menu\n:')
		if update_again_ == 'yes':
			return update()
		elif update_again_ == 'no':
			print('ok!')
			main_menu()


# DELETE A RECORD
def delete():
	print('\nDELETE CONTACT: ')
	while True:
		user_delete_name = input('\ntype the name of the contact that you would like to delete\n:')
		user_delete_name = user_delete_name.lower()
		search_results = {}
		for dictionary in contact_list:
			for key, value in dictionary.items():
				if user_delete_name in value:
					search_results = dictionary
					print(f'CONTACT FOUND:\n{search_results}\n')
					print('is this the contact that you would like to delete?')
					while True:
						user_delete_confirm = input('type "yes" or "no"\n:')
						user_delete_confirm = user_delete_confirm.lower()
						user_delete_final = ''
						if user_delete_confirm == 'yes':
							delete_confirm_final = ''
							while True:
								delete_confirm_final = input('\nare you sure you want to delete this'
								                             ' contact?\ntype "yes" or "no"\n:')
								delete_confirm_final = delete_confirm_final.lower ()
								if delete_confirm_final == 'yes':
									user_delete_final = dictionary
									print(f'\nCONTACT DELETED: {user_delete_final}\n')
									contact_list.remove(user_delete_final)
									print('UPDATED CONTACT LIST: \n')
									view_contacts()
									return delete_again()
								elif delete_confirm_final == 'no':
									print('\nCONTACT DELETION CANCELLED!')
						elif user_delete_confirm == 'no':
							print('\nok let\'s try again!')
							return delete()
		if user_delete_name not in value:
			print('\nsorry! there is no matching contact in the directory\n')
		delete_again()


# CONTINUE DELETING RECORDS
def delete_again():
	delete_again_ = ''
	print('\nwould you like to delete another contact?\n')
	while True:
		delete_again_ = input('type "yes" or "no"\n:')
		delete_again_ = delete_again_.lower()
		if delete_again_ == 'yes':
			return delete()
		elif delete_again_ == 'no':
			print('ok!')
			main_menu()


def main_menu():
	user_main_menu_ = ''
	user_main_menu_ = user_main_menu_.lower ()
	print('\nWELCOME TO CONTACTS!\n\nMAIN MENU:\n'
	      '01- "CREATE" NEW CONTACT\n'
	      '02- "RETRIEVE"/ "SEARCH" CONTACTS\n'
	      '03- "UPDATE" CONTACT\n'
	      '04- "DELETE" CONTACT\n'
	      '05- "VIEW" CONTACTS\n'
	      '06- "EXIT"/ "QUIT"\n')
	while True:
		user_main_menu_ = ''
		user_main_menu_ = input('what would you like to do?\ntype the word in "QUOTE"s to initiate\n:')
		user_main_menu_ = user_main_menu_.lower()
		if user_main_menu_ == 'create':
			new_contact()
			another_contact()
		elif user_main_menu_ == 'retrieve' or user_main_menu_ == 'search':
			lookup()
			lookup_another()
		elif user_main_menu_ == 'update':
			update()
			update_again()
		elif user_main_menu_ == 'delete':
			delete()
			delete_again()
		elif user_main_menu_ == 'view':
			view_contacts()
			main_menu()
		elif user_main_menu_ == 'quit' or user_main_menu_ == 'exit':
			quit()


main_menu()
