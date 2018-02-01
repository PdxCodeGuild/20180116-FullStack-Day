import datetime
#import dash
#import dash_core_components as dcc
#import dash_html_components as html
#import plotly.graph_objs as go
#import plotly.plotly as py
#import plotly.graph_objs as go
import csv
import re
import statistics

#app = dash.Dash()

# Attempted to make a function to open the file here, but it would not recognize that the file was a file. Leaving this for now to come back to later.
'''def load_rain_data(data_file):
    with open(f'{data_file}', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data = file.split('\n')
    return data'''

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
    year2 = int(year2)
    year_dict = {}
    for year in range(year1, year2):
        if year in date_with_data[i][0]:
            year_dict[year] = 0
    for year in year_dict.keys():
        for i in range(len(date_with_data[i][1]), len(date_with_data) + 1):
            try:
                if year in date_with_data[i][0]:
                      year_dict[year] += date_with_data[i][1]
            except:
                pass
    return year_dict


'''

def month_sum(date_with_data, year_month):
    month_dict = {}
    for month in range(int(year_month), int(year_month)):  # Will this give an error?? Probavbly...
        if month in date_with_data[i][0]:
            month_dict[month] = 0
    for month in month_dict.keys():
        for i in range(len(date_with_data[i][1]), len(date_with_data) + 1]):
            try:
                if month in date_with_data[i][0]:
                      month_dict[month] += date_with_data[i][1]
        except:
            pass
    return month_dict
'''
year1 = input(f"What year would you like to start at? 2004 - 2017 are available.\n")
year2 = input(f"What year would you like to end on? 2004 - 2017 are available.\n")

year_sums = year_sum(data_list, year1, year2)

x_axis = []
while i in range(len(date_list)):
    x_axis.append(date_list[i])

y_axis = []
while i in range(len(data_list)):
    y_axis.append(data_list[i][1])





#print(data_list)

#for i in range(len(date_list)):
#    print(date_list[i].year, date_list[i].month, date_list[i].day) # Yep! It prints all the dates

plt.plot(x_axis, y_axis)
plt.show()





'''

# Add data
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]

# Create and style traces
trace0 = go.Scatter(
    x = month,
    y = high_2014,
    name = 'High 2014',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)
trace1 = go.Scatter(
    x = month,
    y = low_2014,
    name = 'Low 2014',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace2 = go.Scatter(
    x = month,
    y = high_2007,
    name = 'High 2007',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dash') # dash options include 'dash', 'dot', and 'dashdot'
)
trace3 = go.Scatter(
    x = month,
    y = low_2007,
    name = 'Low 2007',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dash')
)
trace4 = go.Scatter(
    x = month,
    y = high_2000,
    name = 'High 2000',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dot')
)
trace5 = go.Scatter(
    x = month,
    y = low_2000,
    name = 'Low 2000',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dot')
)
data = [trace0, trace1, trace2, trace3, trace4, trace5]

# Edit the layout
layout = dict(title = 'Average High and Low Temperatures in New York',
              xaxis = dict(title = 'Month'),
              yaxis = dict(title = 'Temperature (degrees F)'),
              )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='styled-line')'''



'''
Download one of these files (or the csv I've compiled containing all of them), and write a function to load the file. Each line of the file will become a list or class or tuple consisting of a datetime and a series of ints.

To parse the dates, use datetime.striptime. Below I've shown how to parse an example string, resulting in a datetime object. We can then access the year, month, and day on that datetime as ints.

import datetime
date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
print(date.year)
print(date.month)
print(date.day)
'''