import datetime
from datetime import datetime
import numpy
import operator
import matplotlib.pyplot as plt

file = 'hayden_island.rain.csv'


def extract_data_from_file(rain_file):
    # original data in 0.01 inches converted to inches
    list_rain_dicts = []
    with open(rain_file, 'r', newline='') as f:
        lines = f.read().split('\n')
        # headers = lines[9].split()
        lines = lines[12:-2]
        for row in lines:
            row = row.split()
            date = datetime.strptime((row[0]), '%d-%b-%Y')
            line_dict = {'date': date, 'year': date.year, 'month': date.month, 'total': float(row[1])*0.01}
            list_rain_dicts.append(line_dict)
    return list_rain_dicts


def all_totals(dict_list):
    data_list = []
    for i in range(len(dict_list)):
        data_list.append(dict_list[i]['total'])
    return data_list


def get_max(dict_list):
    data_list = []
    date_list = []
    for i in range(len(dict_list)):
        data_list.append(dict_list[i]['total'])
        date_list.append(dict_list[i]['date'])
    max_index, max_value = max(enumerate(data_list), key=operator.itemgetter(1))
    max_date = date_list[max_index]
    outstring = f'Date: {max_date.month}-{max_date.day}-{max_date.year}, total: {round(max_value, 2)} inches'
    return outstring


def get_yearly_average(dict_list, year):
    year_data_list = []
    for i in range(len(dict_list)):
        if dict_list[i]['year'] == year:
            year_data_list.append(dict_list[i]['total'])
    year_mean = numpy.mean(year_data_list)
    return year_mean


def calculate_max_year_averages(dict_list):
    year_means = []
    years = []
    # get the total list. Get the year, get the
    for year in range(1998, 2018):
        year_means.append(get_yearly_average(dict_list, year))
        years.append(year)
    max_index, max_value = max(enumerate(year_means), key=operator.itemgetter(1))
    max_year = years[max_index]
    outstring = f'{max_year},  Average: {round(max_value, 2)} inches'
    return outstring


def plot_dates_totals(dict_list):
    dates = []
    totals = []
    for i in range(len(dict_list)):
        dates.append((dict_list[i]['date']))
        totals.append(dict_list[i]['total'])
    plt.plot(dates, totals)
    plt.ylabel('Total collected rainfall in inches')
    plt.xlabel('dates')
    plt.suptitle('Daily rainfall totals: 1998-2018')
    plt.show()


def get_monthly_average_all_years(dict_list, month):
    totals_list = []
    for i in range(len(dict_list)):
        if dict_list[i]['month'] == month:
            totals_list.append(dict_list[i]['total'])
    month_mean = numpy.mean(totals_list)
    return month_mean


def plot_month_averages_all_years(dict_list):
    averages = []
    month_list = []
    for month in range(1, 12):
        averages.append(get_monthly_average_all_years(dict_list, month))
        month_list.append(month)
    plt.plot(month_list, averages)
    plt.ylabel('Average collected rainfall in inches')
    plt.xlabel('Month')
    plt.suptitle('Monthly rainfall averages: 1998-2018')
    plt.show()


def get_yearly_total(dict_list, year):
    totals_list = []
    for i in range(len(dict_list)):
        if dict_list[i]['year'] == year:
            totals_list.append(dict_list[i]['total'])
    year_sum = numpy.sum(totals_list)
    return year_sum


def plot_year_totals(dict_list):
    totals = []
    year_list = []
    for year in range(1998, 2019):
        totals.append(get_yearly_total(dict_list, year))
        year_list.append(year)
    plt.bar(year_list, totals)
    plt.ylabel('Rainfall in inches')
    plt.xlabel('Year')
    plt.suptitle('Total collected rainfall per year: 1998-2018')
    plt.show()


# Statistical function calls
rain_data_dicts = extract_data_from_file(file)
population = all_totals(rain_data_dicts)

pop_sum = str(round(sum(population), 2))
pop_mean = round(numpy.mean(population), 2)
pop_var = round(numpy.var(population),2)
pop_max = get_max(rain_data_dicts)
max_of_year_means = calculate_max_year_averages(rain_data_dicts)


# terminal presentation of statistical calculations
print()
print('Hayden Island Rainfall Data')
print('Values measured in inches of collected rainfall.\n')

print('Data from all years:')
print(f'Total measured rainfall 1998-2018: {pop_sum} inches')
print(f'Mean daily rainfall total: {pop_mean} inches')
print(f'Total Variance of measured data: {pop_var} inches')
print(f'Maximum measurement from all years: {pop_max} inches')
print(f'Year with the highest average rain: {max_of_year_means}')


# plotting some data in matlab
plot_dates_totals(rain_data_dicts)
plot_month_averages_all_years(rain_data_dicts)
plot_year_totals(rain_data_dicts)
