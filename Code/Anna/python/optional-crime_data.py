"""
Optional lab
Sometimes crime does pay
"""


def load(path):
    with open(path, 'r') as f:
        contents = f.read().replace('"', '')
        new_contents = contents.split('\n')
        items = [new_content.split(',') for new_content in new_contents]
    return items


def load_data():
    print("Which year of crime statistics would you like to analyze? Choose a year between 2011 and 2014 or 'recent' for the most recent data.")
    choice = input("> ")

    if choice == 'recent':
        data = load('../../../1 Python/data/crime_incident_data_recent.csv')
        print("\nYou have chosen to look at the most recent crime data from 2014-2015.")
    elif choice == '2014':
        data = load('../../../1 Python/data/crime_incident_data_2014.csv')
        print("\nYou have chosen to look at crime data from 2014.")
    elif choice == '2013':
        data = load('../../../1 Python/data/crime_incident_data_2013.csv')
        print("\nYou have chosen to look at crime data from 2013.")
    elif choice == '2012':
        data = load('../../../1 Python/data/crime_incident_data_2012.csv')
        print("\nYou have chosen to look at crime data from 2012.")
    elif choice == '2011':
        data = load('../../../1 Python/data/crime_incident_data_2011.csv')
        print("\nYou have chosen to look at crime data from 2011.")
    else:
        print("That is not a valid year.")
        return None

    return data


def find_crime_type(data):
    crime_dict = {}
    for i in range(1, len(data)-1):
        if data[i][3] not in crime_dict:
            crime_dict[data[i][3]] = 1
        else:
            crime_dict[data[i][3]] += 1
    return crime_dict


def count_all_crimes():
    with open('../../../1 Python/data/crime_incident_data_recent.csv', 'r') as f:
        contents = f.read().replace('"', '')
        new_contents = contents.split('\n')
        recent_items = [new_content.split(',') for new_content in new_contents]
        recent_len = len(recent_items)
    with open('../../../1 Python/data/crime_incident_data_2014.csv', 'r') as f:
        contents = f.read().replace('"', '')
        new_contents = contents.split('\n')
        items_2014 = [new_content.split(',') for new_content in new_contents]
        len_2014 = len(items_2014)
    with open('../../../1 Python/data/crime_incident_data_2013.csv', 'r') as f:
        contents = f.read().replace('"', '')
        new_contents = contents.split('\n')
        items_2013 = [new_content.split(',') for new_content in new_contents]
        len_2013 = len(items_2013)
    with open('../../../1 Python/data/crime_incident_data_2012.csv', 'r') as f:
        contents = f.read().replace('"', '')
        new_contents = contents.split('\n')
        items_2012 = [new_content.split(',') for new_content in new_contents]
        len_2012 = len(items_2012)
    with open('../../../1 Python/data/crime_incident_data_2011.csv', 'r') as f:
        contents = f.read().replace('"', '')
        new_contents = contents.split('\n')
        items_2011 = [new_content.split(',') for new_content in new_contents]
        len_2011 = len(items_2011)

    max_list = [recent_len, len_2014, len_2013, len_2012, len_2011]

    if recent_len == max(max_list):
        return f"\nThe year with the most crime was {2014-2015}, with {recent_len} crimes."
    elif len_2014 == max(max_list):
        return f"\nThe year with the most crime was {2014}, with {len_2014} crimes."
    elif len_2013 == max(max_list):
        return f"\nThe year with the most crime was {2013}, with {len_2013} crimes."
    elif len_2012 == max(max_list):
        return f"\nThe year with the most crime was {2012}, with {len_2012} crimes."
    elif len_2011 == max(max_list):
        return f"\nThe year with the most crime was {2011}, with {len_2011} crimes."
    else:
        return "Portland is a crime-free paradise!"


data = load_data()  # choose which year to look at
crime_dict = find_crime_type(data)

print("The most frequent crimes that year were:")

tup_crimes = list(crime_dict.items())  # list of tuples
tup_crimes.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(30, len(tup_crimes))):  # print the top 30 crimes, or all of them, whichever is smaller
    print(f"'{tup_crimes[i][0]}' was committed {tup_crimes[i][1]} times")


print(count_all_crimes())
