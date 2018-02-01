import datetime
# from os import getcwd
from datetime import datetime
# import itertools
import numpy

file = 'hayden_island.rain.csv'


def extract_data_from_file(rain_file):
    list_rain_dicts = []
    with open(rain_file, 'r', newline='') as f:
        lines = f.read().split('\n')
        # headers = lines[9].split()
        lines = lines[12:-2]
        headers = ['year', 'month', 'day', 'total']
        for row in lines:
            row = row.split()
            date = datetime.strptime((row[0]), '%d-%b-%Y')
            line_dict = {'date': date.year, 'month': date.month, 'day': date.day, 'total': int(row[1])}
            list_rain_dicts.append(line_dict)
    return list_rain_dicts


def all_totals(list_rain_dicts):
    data_list = []
    for i in range(len(list_rain_dicts)):
        data_list.append
    return data_list


def get_year_data(dict_list, year):
    data_list = []
    for i in range(len(dict_list)):
        if dict_list[i]['year'] == year:
            data_list.append(dict_list[i])
            print(year)
    return data_list


def get_month_data(dict_list, month):
    data_list = []
    for i in range(len(dict_list)):
        if dict_list[i]['month'] == month:
            data_list.append(dict_list[i]['total'])
    return data_list


def get_day_data(dict_list, day):
    data_list = []
    for i in range(len(dict_list)):
        if dict_list[i]['day'] == day:
            data_list.append(dict_list[i]['total'])
    return data_list


rain_data_dicts = extract_data_from_file(file)
population = all_totals(rain_data_dicts)

pop_sum = sum(population)
pop_mean = numpy.mean(population)
pop_var = numpy.var(population)

print(pop_sum)
print(pop_mean)
print(pop_var)
