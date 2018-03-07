

# Open csv file and write lines to list named contacts
with open('contacts.csv', 'r') as file:
    contacts = list()
    lines = file.read()
    lines = lines.split('\n')
    for line in lines:

        line = line.split(',')
        if line[0] == 'name':
            continue
        else:
            contacts.append({'name':line[0], 'favorite fruit':line[1], 'favorite color':line[2], 'phone number': line[3]})


# Function that checks if a name is already associated withe a record,
# returns record index or -1 if not present
def check_for_record(data_set, name):
    for item in data_set:
        if item['name'] == name:
            return data_set.index(item)
    return -1

# Lets a user create a new record by name, unless name already exists
def create_record(data_set):
    record = dict()
    while True:
        record_name = input('Please enter the name of the record you wish to update: ')
        record_index = check_for_record(data_set, record_name)
        if record_index == -1:
            record['name'] = record_name
            record['favorite fruit'] = input('Enter the favorite fruit: ')
            record['favorite color'] = input('Enter the favorite color')
            record['phone number'] = input('Enter the phone number')
            data_set.append(record)
            print('Created record for ' + record_name)
            return data_set
        else:
            print('A record already exists for ' + record_name)

# Lets a user update a record, finding a record by name
def update_record(data_set):
    record = dict()
    while True:
        record_name = input('Please enter the name of the record you wish to update: ')
        record_index = check_for_record(data_set, record_name)
        if record_index > -1:
            record['name'] = record_name
            record['favorite fruit'] = input('Enter the favorite fruit: ')
            record['favorite color'] = input('Enter the favorite color: ')
            record['phone number'] = input('Enter the phone number')
            data_set[record_index] = record
            print('Updated ' + record_name)
            return data_set
        else:
            print('That record was not found, please enter another: ')

# Lets a user delete a record, selecting record by name
def delete_record(data_set):
    while True:
        record_name = input('Please enter the name of the record you wish to delete: ')
        record_index = check_for_record(data_set, record_name)
        if record_index > -1:
            data_set.pop(record_index)
            print('Deleted ' + record_name)
            return data_set
        else:
            print('That record was not found, please enter another: ')

# Lets a user retrieve a record, selecting record by name
def retrieve_record(data_set):
    record = dict()
    while True:
        record_name = input('Please enter the name of the record you wish to retrieve: ')
        record_index = check_for_record(data_set, record_name)
        if record_index > -1:
            print(data_set[record_index])
            return data_set
        else:
            print('That record was not found, please enter another: ')

# Prints all records in the data set
def print_record(data_set):
    for item in data_set:
        print(item)
    return data_set

def send_sms(data_set):
    pass


# Get user choice
while True:
    print('1) Create Record\n2) Update a record\n3) Delete a record\n'
          '4) Retrieve a record\n5) Print all records\n6) Send and SMS\n 7) Quit ')
    choice = input('Please enter your choice: ')
    try:
        choice = int(choice)
    except ValueError:
        print('Please enter an integer')
    if choice == 7:
        break

    # A list of function calls
    functions = [create_record, update_record, delete_record, retrieve_record, print_record, send_sms]
    contacts = functions[choice-1](contacts)


# Write data set to contacts.csv
with open('contacts.csv', 'w') as file:
    print('Writing your contacts to file...')
    lines = list()
    for record in contacts:
        line = ','.join([record['name'], record['favorite fruit'], record['favorite color'], record['phone number']])
        lines.append(line)
    lines = '\n'.join(lines)
    file.writelines(lines)


print('Done')
print('Goodbye')