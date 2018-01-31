# Rain Data
import datetime
################################################################################################################
def read_file():
    with open('hayden_island.rain.csv', 'r') as file:
        f = file.read().split('\n')
        my_list = []

        for line in f:
            my_list.append(line.split())

    # del -> deletes the first 2 (0 and 1) of the lines we don't need.
    # each line is in a list so when it deletes a line it deletes index 0
    # in my_list[0] and index 1 in my_index[1]
    del my_list[0:2]

    # These check print statements will show you how my_list[0][0] has a date now.
    # in the double list [0][0] the first Zero in square brackets is the first list index
    # the second zero in square brackets is the first string of the first index.
    # print(my_list[0])  # Complete Date: prints -> ['29-JAN-2018', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '3', '0']
    # print(my_list[0][0]) # Date 1 of the complete date prints -> 29-JAN-2018
    # print(my_list[1][0]) # Date 2 on the next list item.
    print(my_list)
    return my_list
################################################################################################################
def dates_file(weather_data):
    date_information = []
    # First i take the lists of lists that comes in and i get
    # only the date from inside of it and i store it into a new
    # list with only dates.
    for index in range(len(weather_data) - 1):
        date_information.append(weather_data[index][0])


    formatted_date = []
    # Then i create a new list in which i will append the formatted dates. The for loops
    # will go through my list of UNFORMATTED dates and format them into a new list.
    for i in range(len(date_information)):
        formatted_date.append(datetime.datetime.strptime(date_information[i], '%d-%b-%Y'))


    # Return a list of formatted dates
    return formatted_date
################################################################################################################


# Version 1
weather_data = read_file()
date_list_format = dates_file(weather_data)

# version 2


################################################################################################################
