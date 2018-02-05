"""
Using matplotlib create a chart of the dates and the daily totals for a given year. The x_values will be a list of
dates, The y_values are a list of the daily totals. If you don't have matplotlib installed, run pip install matplotlib.
You can learn more about matplotlib here.

import matplotlib.pyplot as plt
...
plt.plot(x_values, y_values)
plt.show()
Some charts you can make are:

all the data, date vs daily total
monthly totals, average across multiple years
total yearly rainfall, year by year
"""

"""
                        Version 1 code here:

Calculate the mean of the data.

Use the mean to calculate the variance:

Find the day which had the most rain on average.

Find the year which had the most rain on average.
"""


"""
Download one of these files (or the csv I've compiled containing all of them), and write a function to load the file.
Each line of the file will become a list or class or tuple consisting of a datetime and a series of ints.

"""
import datetime



def load_data(file):
    #load the file
    # nameoffile = input('what is the name of the file that you would like the ARI computed for (add .txt): ')

    with open(file) as f:  # open the file. file was downloaded and added to repository
        contents = f.read().split('\n')  # splits every new line
        #contents = f.read()  # list of all the lines as strings (not sentences)

    daily_total_tuples_in_list = []
    for i in range(12,len(contents)):
        line = contents[i].split() # line is a list of strings, because split() with no parameters splits on spaces/tabs
        #print(line)
        # data_name = contents[i][:11]
        # data_name = []
        if len(line) == 0:
            continue  # skips over empty lines, there was one at the end
        date_str = line[0] # date and time are at index 0
        date = datetime.datetime.strptime(date_str, '%d-%b-%Y') #convert to a 'datetime' data type
        if line[1] == '-':
            continue  # skips over hyphens for days that don't work
        daily_total_str = int(line[1])
        daily_total_tuples_in_list.append((date, daily_total_str))
    return daily_total_tuples_in_list


daily_total_tuples_in_list = load_data('RainyDay.txt')

# print(daily_total_tuples_in_list)




"""Version 2 starts here"""

# use daily_total_tuple to calculate mean

sum = 0
n = 0
for i in range(len(daily_total_tuples_in_list)):
    sum += daily_total_tuples_in_list[i][1]
    n += 1

# print(sum)
# print(n)

mean = sum/n
# print(mean)
mean_inches = round((sum/n)/ 100, 2) # 100 because data was measuring .01 inches

print(f'The average daily rainfall is {mean_inches} inches')

# Calculate the variance
var_dif = 0
sum_var = 0
for i in range(len(daily_total_tuples_in_list)):
    var_dif = daily_total_tuples_in_list[i][1] - mean
    # print(var_dif)
    sq_var = var_dif ** 2
    sum_var += sq_var
var = sum_var /n
var_inches = round((var/100), 2)
print(f'The variance is {var_inches}')

# Find the day which had the most rain on average

x = daily_total_tuples_in_list[0][1]
date = daily_total_tuples_in_list[0][0]
for i in range(1, len(daily_total_tuples_in_list)):
    if x < daily_total_tuples_in_list[i][1]:
        x = daily_total_tuples_in_list[i][1]
        date = daily_total_tuples_in_list[i][0]
x_inches = round(x / 100, 2)

print(f'{date.strftime("%d-%b-%Y")} was the wettest day on record with {x_inches} inches of rain')


# find the year which had the most rain on average

rain_total_overall = 0
rain_total_current = 0
most_rain_year = 0
for i in range(len(daily_total_tuples_in_list)):
    current_date = daily_total_tuples_in_list[i][0]
    rain_total_current += daily_total_tuples_in_list[i][1]
   # print(rain_total_current)
   # print(daily_total_tuples_in_list[i][0].year)
    if current_date.month == 12 and current_date.day == 31: #this was not working
        #print(rain_total_current)
        if rain_total_current > rain_total_overall:
            rain_total_overall = rain_total_current
            most_rain_year = current_date.year
        rain_total_current = 0
rain_total_in_inches = rain_total_overall / 100

print(f'{most_rain_year} was the wettest year on record with a total rainfall of {rain_total_in_inches} inches')


""" Version 3 starts here"""
import Lab024_RainData_v2
import matplotlib.pyplot as plt

x_values = []
y_values = []

# The x_values will be a list of dates, The y_values are a list of the daily totals.
for i in range(len(daily_total_tuples_in_list)):
    x_values.append(daily_total_tuples_in_list[i][0])
    y_values.append(daily_total_tuples_in_list[i][1])

plt.plot(x_values, y_values)
plt.xlabel('daily rain totals 1998-2018')
plt.ylabel('rain in 0.01 inches')
plt.title('Daily Rain total in Portland, OR')
plt.show()