# CSV Files
import csv
########################################################################
# read file is a little different here. I imported csv so that i could
# cast it into a lists of lists. When i parse it it helps me break it up
# easier into a list of dictionaries. 
def read_csv_file():
    with open('names_colors.csv') as csv_file:
        file_content = list(csv.reader(csv_file))

    return file_content
########################################################################
# I write it into another file just so that i don't mess up my current file.
# but the csv could be the same as in read file function. 
def write_to_csv_file(updated_list):
    # with open('names_color_write.csv', 'w') as written_file:
    #         written_file.write(str(updated_list))
    with open('names_color_write.csv', 'w') as file:
        file.write("first_name,last_name,fav_color\n")
        for i in range(len(updated_list)):
            file.write(updated_list[i]['first_name']+ ',' +
                       updated_list[i]['last_name'] + ',' +
                       updated_list[i]['fav_color'] + '\n')
            
########################################################################
# I .pop() the last part because the first values for keys: first_name last_name and fav_color
# are the same. So popping the first value eliminates that. However i had to add it back
# when i write to the new file.  
def parse_file(file_content):
    contact_list = []
    i = 0
    for value in file_content:
        dictionary = {}
        while i < 3:
            dictionary[file_content[0][i]] = value[i]
            i += 1
        i = 0
        contact_list.append(dictionary)
    contact_list.pop(0)
    
    return contact_list
########################################################################
# You don't need a for loop to append. 
def create_record(parsed_file):
    # first_name,last_name,fav_color
    # Ask user for each of the header attribute So that it creates a new record and store the record
    # with .append() at the end of the list of dictionaries.
    f_name = input("What is the first name: ")
    l_name = input("What is the last name: ")
    favorite_color = input(f'What is {f_name} {l_name}\'s favorite Color: ')
    parsed_file.append({'first_name': f_name, 'last_name': l_name, 'fav_color': favorite_color})
    return parsed_file


########################################################################
def look_for_record(parsed_file):
    # ask the user for the contact's name, find the user with the given name, and display their information
    f_name = input("What is the first name in the file: ")
    l_name = input("What is the last name in the file: ")

    for value in range(len(parsed_file)):
        if parsed_file[value]['first_name']  == f_name and parsed_file[value]['last_name'] == l_name:
            print(f'{parsed_file[value]["first_name"]} {parsed_file[value]["last_name"]} '
                  f'favorite color is {parsed_file[value]["fav_color"]}')
    return parsed_file

########################################################################
def update_record(parsed_file):
    # ask the user for the contact's name, then for which attribute of the user
    # they'd like to update and the value of the attribute they'd like to set
    f_name = input('What is the first name of the file you want to change: ')
    l_name = input('What is the last name of the file you want to change: ')
    word_change = input(f'What is the new favorite color for {f_name} {l_name}: ')

    for value in range(len(parsed_file)):
        if parsed_file[value]['first_name']  == f_name and parsed_file[value]['last_name'] == l_name:
            parsed_file[value]['fav_color'] = word_change
            print(f'The new update for {f_name} {l_name} is {parsed_file[value]["fav_color"]}')

    return parsed_file

########################################################################
# The delete_record() function will go through the entire for loop an check
# if the first name and last name match and it will use the del object to
# delete the entire value of the dictionary. 
def delete_record(parsed_file):
    # ask the user for the contact's name, remove the contact with
    # the given name from the contact list
    f_name = input('What is the first name of the file you want to delete: ')
    l_name = input('What is the last name of the file you want to delete: ')
    print(parsed_file)

    for value in range(len(parsed_file) - 1):
        if parsed_file[value]['first_name']  == f_name and parsed_file[value]['last_name'] == l_name:
            del parsed_file[value]
            

    return parsed_file
########################################################################
def ask_user(parsed_file):
    updated_list = []
    user_input = input("What do you want to do? Type -> "
                       "Create, Lookup, Update, or Delete : ").lower()

    if user_input == 'create':
        updated_list = (create_record(parsed_file))
    elif user_input == 'lookup':
        updated_list = look_for_record(parsed_file)
    elif user_input == 'update':
        updated_list = update_record(parsed_file)
    elif user_input == 'delete':
        updated_list = delete_record(parsed_file)

    return updated_list


########################################################################
# CALL FUNCTIONS

# Version 1
file_content = read_csv_file()
parsed_file = parse_file(file_content)

# Version 2
updated_list = ask_user(parsed_file)

# Version 3
write_to_csv_file(updated_list)


