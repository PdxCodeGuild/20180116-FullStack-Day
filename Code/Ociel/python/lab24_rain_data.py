# Rain Data
import datetime
import matplotlib.pyplot as plt
################################################################################################################
# Inside READ FILE
# Note 1 -The first split('\n') will take the first line and
#         when it sees an invisible \n in the file it will
#         then create another string inside the list. Not another list.
#         One list with several strings inside.
#Note 2 - The second split is needed because it will put each string
#         into a list and separate make the strings inside each have
#         and individual index. Read comment below.
# Note 3 - del -> deletes the first 2 (0 and 1) of the lines we don't need.
#         each line is in a list so when it deletes a line it deletes index 0
#         in my_list[0] and index 1 in my_index[1]
# Note 4 - These check print statements will show you how my_list[0][0] has a date now.
# in the double list [0][0] the first Zero in square brackets is the first list index
# the second zero in square brackets is the first string of the first index.
# print(my_list[0])  # Complete Date: prints -> ['29-JAN-2018', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '3', '0']
# print(my_list[0][0]) # Date 1 of the complete date prints -> 29-JAN-2018
# print(my_list[1][0]) # Date 2 on the next list item.
def read_file():
    with open('hayden_island.rain.csv', 'r') as file:
        # Note 1
        f = file.read().split('\n')
        my_list = []
        # Note 2
        for line in f:
            my_list.append(line.split())

    # Note 3
    del my_list[0:2]
    # Note 4
    return my_list
################################################################################################################
# Inside DATES FILE
# Notes 1 -First i take the lists of lists that comes in and i get
#          only the date from inside of it and i store it into a new
#          list with only dates.
# Notes 2 - Then i create a new list in which i will append the formatted dates. The for loops
#           will go through my list of UNFORMATTED dates and format them into a new list.

def dates_file(weather_data):
    date_information = []
    # Note 1
    for index in range(len(weather_data) - 1):
        date_information.append(weather_data[index][0])
    formatted_date = []
    # Note 2
    for i in range(len(date_information)):
        formatted_date.append(datetime.datetime.strptime(date_information[i], '%d-%b-%Y'))
    # Return a list of formatted dates
    return formatted_date
################################################################################################################
# INSIDE GET NUMBER DATA
# WeatherData is a list of lists
# NOTE 1 - The first loop deletes the All the lists first index which is a date. Then it stores it
#          inside a new list. Which is still a list of lists but the numbers inside are still strings.
# Note 2 - The second loop has two loops . The first loop goes through LENGTH of the the List and the
#          second loops goes through the length size of each individual list. That is why i can
#          go through each number in the list and make them an integer.
# Note 3 - The reason i have the numbers_as_integers outside the second for-loop is because it will make it again
#          into a list of lists. if i don't have it inside the first loops it will store it into
#          numbers[] as one list with numbers but i want to separate each line into it's own
#          category for future use.

def get_number_data(weather_data):

    numbers_with_removed_dates_still_strings= []
    # Note 1
    for index in range(len(weather_data) - 1):
        del weather_data[index][0]
        numbers_with_removed_dates_still_strings.append(weather_data[index])


    numbers = []
    # Note 2
    for index in range(len(numbers_with_removed_dates_still_strings)):
        # Note 3
        numbers_as_integers = []
        for length_of_elements_inside_list in range(len(numbers_with_removed_dates_still_strings[index])):
             numbers_as_integers.append(int(numbers_with_removed_dates_still_strings[index][length_of_elements_inside_list]))
        numbers.append(numbers_as_integers)

    return numbers
################################################################################################################
# Inside Totals
# Gets the element of every list which is the totals numbers and stores it into one list with the values taken.
def totals_of_each_day(numbers_list):
    totals = []
    for value in numbers_list:
        totals.append(value[0])
    # Returns the list of only the totals.
    return totals

################################################################################################################
def get_mean(totals_list):
    sum = 1
    total_numbers = len(totals_list)
    # Note 1
    for value in totals_list:
        sum += value

    return sum / total_numbers

################################################################################################################
# Inside GET VARIANCE
# Note 1 - I only get the totals which is the first value of every list. I subtract the mean and square it.
def get_variance(totals_list, mean):
    sum = 0
    # Note 1
    for value in totals_list:
        sum += (value - mean) **2

    return sum / len(totals_list)


################################################################################################################

def find_day_and_year_with_most_rain(date_list, totals_list):
    max_value = max(totals_list)
    index_value_of_max = totals_list.index(max_value)
    day = date_list[index_value_of_max].day
    year = date_list[index_value_of_max].year
    print(f'The day that had the most rain was {day}. ')
    print(f'The day that had the most rain was {year}.')
################################################################################################################
# Inside MAKE CHART
# X (Horizontal Line) is the dates list
# Y (Vertical Line) is the totals list
def make_chart(x,y):
    plt.plot(x,y)
    plt.show()

################################################################################################################
# Call functions
# Version 1
weather_data = read_file()
date_list_format = dates_file(weather_data)

# version 2
numbers_list = get_number_data(weather_data)
totals_list = totals_of_each_day(numbers_list)
mean = get_mean(totals_list)
variance = get_variance(totals_list, mean)
find_day_and_year_with_most_rain(date_list_format,totals_list)

# Version 3
make_chart(date_list_format,totals_list)

################################################################################################################
