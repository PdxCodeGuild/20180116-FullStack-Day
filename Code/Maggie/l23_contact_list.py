# Let's build a program to manage a list of contacts.
from csv import DictReader, writer
from collections import OrderedDict


class Contactlist:  # Create/Read/Update/Delete Information Storage
    contact_list = []
    fieldnames = ['name', 'favorite fruit', 'favorite color']

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_csv(self):
        with open(self.csv_file, 'r') as file:  # open for reading
            for line in DictReader(file):
                self.contact_list.append(line)
        print(f'{self.csv_file} Contact list loaded!')
        return self.contact_list

    def write_csv(self):
        new_file = 'new_file.csv'
        with open(new_file, 'w') as csv_file:
            write = writer(csv_file)
            write.writerow(self.fieldnames)
            for i in range(len(self.contact_list)):
                line_data = (f'{val}' for key, val in self.contact_list[i].items())
                write.writerow(line_data)
        print(f'file saved to {new_file}')

    def create(self):  # add a new entry to the contact list at the end
        contact = OrderedDict()  # an entry is stored in a dictionary
        new_name = input('Contact name: ')
        new_fruit = input(f'{new_name}\'s favorite fruit: ')
        new_color = input(f'{new_name}\'s favorite color: ')
        contact['name'] = new_name
        contact['favorite fruit'] = new_fruit
        contact['favorite color'] = new_color
        self.contact_list.append(contact)

    def retrieve(self):  # pull up a record by name, display information
        found = False
        print('Please enter a name to look up a record.')
        contact_name = input('Contact name: ')
        for i in range(len(self.contact_list)):
            if self.contact_list[i]['name'] == contact_name:
                index = i
                self.print_record(index)
                return index
        if not found:
            print('Sorry. That entry does not appear to be in the contact list.')

    def update(self, index):
        print('UPDATE')
        key_search_term = input('Which item would you like to change? ')
        if key_search_term in self.contact_list[index]:
            print(self.contact_list[index][key_search_term])
            replacement_value = input('What would you like to change this to?')
            self.contact_list[index][key_search_term] = replacement_value
            print(self.contact_list[index])
        else:
            print('Sorry, that key was not found')
            print('would you like to add a new field?')
            u_choice = input('Your choice: ')
            if u_choice == 'y':
                self.add_new_key_val_pair(index)

    def add_new_key_val_pair(self, index):
        new_key = input('enter a new field.')
        new_value = input(f'enter a {new_key}')
        self.contact_list[index][new_key] = new_value
        self.fieldnames.append(new_key)

    def delete_record(self, index):
        self.contact_list.pop(index)
        print('Record deleted')

    def print_record(self, index):
        record_disp = '\n'.join(f'{key}: {val}' for key, val in self.contact_list[index].items())
        print('\nContact found:', record_disp, '\n')

    def decide(self, choice):
        try:
            if choice == '1':
                self.create()
            elif choice == '2':
                self.retrieve()
            elif choice == '3':
                index = self.retrieve()
                self.update(index)
            elif choice == '4':
                index = self.retrieve()
                self.delete_record(index)
            elif choice == 'q':
                print('goodbye.')
            elif choice == 's':
                self.write_csv()

            else:
                print('invalid choice.')
        except KeyError:
            print('Invalid choice.')


def load_script():
    ascii_art = '''
                  (\_/) 
                  'o.o' 
==================(_ _)====================
Contact list v0.1   U   Maggie Geise, 2018\n'''
    print(ascii_art)


def __main__():
    load_script()
    filename = 'contacts.csv'
    contacts = Contactlist(filename)
    Contactlist.read_csv(contacts)
    header_text = 'Select from the list of options.'
    select = '\t1. Create a new entry.\n\t2. Retrieve an existing entry' \
             '\n\t3. Update an existing entry.\n\t4. Delete an entry.' \
             f'\n\ts. Save {filename}\n\tq. Quit'
    while True:
        print(header_text)
        print(select)
        u_prompt = input('Your choice: ')
        try:
            Contactlist.decide(contacts, u_prompt)
            if u_prompt.lower() == 'q':
                break
        except KeyError:
            print('Invalid choice. Try again.')


__main__()
