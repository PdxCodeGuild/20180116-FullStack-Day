import datetime

import matplotlib.pyplot as plt


def mean_fall(data):
    total = 0
    non = 0
    for days in range(len(data)):
        if data[days][1] == '-':
            non += 1
            continue
        else:
            total += int(data[days][1])
    mean = total / (len(data) - non)
    print(mean)
    return mean


def variance(data, average):
    sum_var = 0
    non_data = 0
    for days in range(len(data)):
        if data[days][1] == '-':
            non_data += 1
            continue
        else:
            sum_var += (int(data[days][1]) - average) * (int(data[days][1]) - average)
    var = sum_var / (len(data) - non_data)
    print(var)
    return var


def most_rain_day(data):
    most = 0
    for days in range(len(data)):
        if data[days][1] == '-':
            continue
        elif int(data[days][1]) > int(most):
            date = data[days]
            most = data[days][1]
        else:
            continue
    print(f'The date with the highest rainfall in a single day is {date[0].year}, {date[0].month}, {date[0].day},')
    print(f'with {most}')


def most_rain_year(data):
    c_year = int(data[0][0].year)
    year_tots = []
    rain_sum = 0
    day_count = 0
    for days in range(len(data)):
        if data[days][1] == '-':
            continue
        if int(data[days][0].year) == c_year:
            rain_sum += int(data[days][1])
            day_count += 1
        else:
            year_tots.append(rain_sum / day_count)
            c_year -= 1
            rain_sum = 0
            day_count = 0
    print(year_tots)


#def graph_data(x, y):
    #for i in range(len(x)):



with open('rain_data.csv', 'r') as file:
    lines = file.read().split('\n')


days_data = []

date = []

for i in range(11, len(lines)):
    digits = lines[i].split()
    date = datetime.datetime.strptime(digits[0], '%d-%b-%Y')
    digits[0] = date
    days_data.append(digits)

#variance(days_data, mean_fall(days_data))
most_rain_year(days_data)




