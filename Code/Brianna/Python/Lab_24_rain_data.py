import datetime
import re
import statistics
import matplotlib.pyplot as plt

# Accessing the file with the data.
with open('airport_way.csv', 'r') as file:
    data = file.read().split('\n')
    print(data)

# Creating a list for data to go into and making it into a list of data.
data_list = []
for i in range(len(data)):
    data_list.append(re.split('\s+', data[i]))  # Need to read more re documentation to understand this a little better.

# Making a copy of my data in case I need it later.
copy_data = data_list.copy()

# Should think of renaming. The is DATE not DATA. Making alist for the date information to go.
date_list = []

for dates in range(len(data_list)):
    if len(data_list[dates][0]) > 8:
        date_list.append(datetime.datetime.strptime(data_list[dates][0], '%d-%b-%Y'))  # for some reason this adds on two 0's to the end of the date data. Not sure why. Possibly time info that is blank?
    else:
        pass


def year_sum(date_with_data, year1, year2):
    year1 = int(year1)
    year2 = int(year2) + 1
    year_dict = {}
    for year in range(year1, year2):
        for i in range(len(date_with_data) - 1):
            if str(year) in date_with_data[i][0]:
                year_dict[year] = 0
    for year in year_dict.keys():
        for i in range(len(date_with_data) - 1):
            if str(year) in date_with_data[i][0]:
                year_dict[year] += int(date_with_data[i][1])

    return year_dict

year1 = input(f"What year would you like to start at? 2004 - 2017 are available.\n")
year2 = input(f"What year would you like to end on? 2004 - 2017 are available.\n")

year_sums = year_sum(data_list, year1, year2)
print(year_sums)

x_axis = year_sums.keys()
y_axis = year_sums.values()



plt.plot(x_axis, y_axis)
plt.show()
print(data_list)



