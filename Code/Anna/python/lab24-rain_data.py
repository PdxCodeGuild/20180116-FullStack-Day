"""
Lab 24
But it never rains in Portland...
"""

import requests
import datetime
import re

r = requests.get('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain')    # because text files are for chumps
data = r.text.split('\n')       # listify

for i in range(0, 12):          # removing comments in the beginning
    data.remove(data[0])
data.pop()                      # removing last blank line

split_data = []
for i in range(len(data)):
    split_data.append(re.split('\s+', data[i]))

print(split_data)

for i in range(len(split_data)):
    date = datetime.datetime.strptime(split_data[i][0], '%d-%b-%Y')
    # print(date.year)
    # print(date.month)
    # print(date.day)

# Version 2

sum_list = []
for i in range(len(split_data)):
    try:
        sum_list.append(int(split_data[i][1]))
    except ValueError:
        sum_list.append(0)

print(sum_list)

total = len(sum_list)
sums = 0
for i in range(len(sum_list)):
    sums += sum_list[i]


def get_mean(total, sums):                          # get the mean
    mean = (1 / total) * sums
    return mean


# sums_list - mean for each sum, then squared
def get_var(mean):                                 # get the variance
    variance = 0
    for i in range(len(sum_list)):
        variance += (sum_list[i] - mean) ** 2
    var = (1 / total) * variance
    return var


mean = get_mean(total, sums)
variance = get_var(mean)

print(f"The mean of the data is: {round(mean, 2)}")
print(f"The variance of the data is: {round(variance, 2)}")


# find the rainiest day

rainy_day = max(sum_list)
rainiest_day = int(sum_list.index(rainy_day))

print(split_data[rainiest_day])
print(f"\nThe rainiest day was {split_data[rainiest_day][0]} with {round(float(rainy_day) * 0.01, 2)} inches of rain!")

# find the rainiest year

year_list = []
for i in range(len(split_data)):
    date = datetime.datetime.strptime(split_data[i][0], '%d-%b-%Y')
    year_list.append(date.year)

# compare year_list with sums_list

year_dict = {}
# year dict will be {year: total sum, year: total sum, year: total sum, etc.}


def match_year():
    for i in range(len(sum_list)):
        if year_list[i] not in year_dict:
            year_dict[year_list[i]] = sum_list[i]
        elif year_list[i] in year_dict:
            year_dict[year_list[i]] += sum_list[i]

    return year_dict


match_dict = match_year()
rainy_year = max(match_dict, key=match_dict.get)
rainy_year_amount = match_dict[rainy_year]

print(f"\nThe rainiest year was {rainy_year} with {round(float(rainy_year_amount) * 0.01, 2)} inches of rain!")