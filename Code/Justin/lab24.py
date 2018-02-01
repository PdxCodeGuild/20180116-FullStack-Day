import datetime
import math
import matplotlib.pyplot as plt

with open('astor.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line != '']


# Find the line of dashes that seperates data column names from data
for i in range(len(lines)):
    if '---------------------' in lines[i]:
        hash_line_index = i
        data_start_index = i + 1
        header_index = i - 1
        break

# Isolate header as a list of column names
header = lines[header_index].split()


# Converts data values to integers if possible else it returns None
def convert_value(value):
    try:
        return int(value)
    except:
        return None


# Make initial data set by splitting lines
data = [line.split() for line in lines[data_start_index:]]

# Get a list of line lengths then find the max line length
line_lengths = [len(line) for line in data]
max_line_length = max(line_lengths)
for i in range(len(data)):
    while len(data[i]) < max_line_length:
        data[i].append(None)

# Make a list of dates as datetime objects
dates = [datetime.datetime.strptime(line[0], '%d-%b-%Y') for line in data]


# Make a list of daily totals, by index these match to items in dates_list
daily_totals = [convert_value(line[1]) for line in data]
hourly_amounts = list()
for i in range(len(data)):
    hourly_amounts.append([convert_value(value) for value in data[i][2:]])
# print(hourly_amounts)
# print(len(hourly_amounts))




# Create a nested dictionary for {years: {stats for year}}
years = set([item.year for item in dates])
stats_by_year = dict()
for year in years:
    stats_by_year[year] = {'dates': [], 'daily totals': [], 'hourly amounts': [], 'year total': 0.0, 'year average': 0.0, 'year variance': 0.0}


for i in range(len(dates)):
    stats_by_year[dates[i].year]['dates'].append(dates[i])
    stats_by_year[dates[i].year]['daily totals'].append(daily_totals[i])
    stats_by_year[dates[i].year]['hourly amounts'].append(hourly_amounts[i])

for year in years:
    stats_by_year[year]['year total'] = sum([value for value in stats_by_year[year]['daily totals'] if value != None])

    if None not in stats_by_year[year]['daily totals']:
        # Compute mean of year's daily totals
        mean = sum(stats_by_year[year]['daily totals']) / len(stats_by_year[year]['daily totals'])
        stats_by_year[year]['year average'] = mean
        # Compute variance of year's daily totals
        variance = sum([((value - mean) ** 2) for value in stats_by_year[year]['daily totals']]) / len(stats_by_year[year]['daily totals'])
        stats_by_year[year]['year variance'] = variance
    else:
        stats_by_year[year]['year average'] = None
        stats_by_year[year]['year variance'] = None


# Print stats_by_year dictionary
for year in sorted(stats_by_year.keys()):
        print('Year: ', year)
        print('List of dates: ', stats_by_year[year]['dates'])
        print('List of daily totals: ', stats_by_year[year]['daily totals'])
        print('List of hourly amounts: ', stats_by_year[year]['hourly amounts'])
        print('Year total: ', stats_by_year[year]['year total'])
        if stats_by_year[year]['year average'] != None:
            print(round(stats_by_year[year]['year average'], 2))
            print(round(stats_by_year[year]['year variance'], 2))

        else:
            print('Year average: ', stats_by_year[year]['year average'])
            print('Year Variance: ', stats_by_year[year]['year variance'])

        print('*' * 200)


# Find max rainfall by day, records max rainfall for more than one day
max_indices = []
max_rainfall = 0.0
for i in range(len(daily_totals)):
    if daily_totals[i] != None:
        if daily_totals[i] > max_rainfall:
            max_indices = []
            max_rainfall = daily_totals[i]
        if daily_totals[i] == max_rainfall:
            max_indices.append(i)

print('Max Rainfall: ', max_rainfall, ' on these dates:')
for i in range(len(max_indices)):
    print(dates[max_indices[i]])

max_years = []
max_average = 0.0
for year in sorted(years):
    if stats_by_year[year]['year average'] != None and year != 2018:
        if stats_by_year[year]['year average'] > max_average:
            max_years = []
            max_average = stats_by_year[year]['year average']
        if stats_by_year[year]['year average'] == max_average:
            max_years.append(year)


print('Max Average: ', max_average, ' in these years:')
for year in max_years:
    print(year)




means = []
for year in sorted(years):
    means.append(stats_by_year[year]['year average'])


# plt.plot(sorted(years), means)
# plt.show()