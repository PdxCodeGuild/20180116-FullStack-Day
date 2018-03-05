import csv
import datetime, time
from matplotlib import pyplot as plt
import pandas as pd

crime_data_2014 = pd.read_csv('crime_incident_data_2014.csv')


x_min = crime_data_2014['X Coordinate'].min()
x_max = crime_data_2014['X Coordinate'].max()
y_min = crime_data_2014['Y Coordinate'].min()
y_max = crime_data_2014['Y Coordinate'].max()

print(x_min)
print(x_max)
print(y_min)
print(y_max)
x_diff = x_max - x_min
y_diff = y_max - y_min
print(x_diff, y_diff)


def adjust_x (x):
    return round((x - x_min) * 2000 / x_diff, 0)


def adjust_y (y):
    return round((y - y_min) * 2000 / y_diff, 0)



crime_data_2014['Adjusted X'] = crime_data_2014['X Coordinate'].apply(adjust_x)
crime_data_2014['Adjusted Y'] = crime_data_2014['Y Coordinate'].apply(adjust_y)

print(crime_data_2014['Adjusted X'].min())
print(crime_data_2014['Adjusted X'].max())
print(crime_data_2014['Adjusted Y'].min())
print(crime_data_2014['Adjusted Y'].max())

crime_data_2014.to_csv('crime_data_2014_adjusted.csv', sep=',')

#
plt.scatter(crime_data_2014['Adjusted X'], crime_data_2014['Adjusted Y'], s=.05)
ax = plt.subplot()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)


plt.show()