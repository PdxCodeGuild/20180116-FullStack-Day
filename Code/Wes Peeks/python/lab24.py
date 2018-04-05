import datetime
import matplotlib.pyplot as plt


def comma_sep():
    with open('marine_drive.csv', 'r') as file:
        f = file.read().split('\n')
        rain_data_list = []
        for data in f:
            rain_data_list.append(data.split())


    del rain_data_list[:2]

    return rain_data_list


def rain_dates(rain):
    r_date = []
    for i in range(len(rain)-1):
        r_date.append(rain[i][0])

    new_dates = []

    for i in range(len(r_date)):
        new_dates.append(datetime.datetime.strptime(r_date[i], '%d-%b-%Y'))
        return new_dates


def rain_numbers(rain_num):
    rain_in_numbers = []

    for i in range(len(rain_num)-1):
        del rain_num[i][0]
        rain_in_numbers.append(rain_num[i])

    numbers = []

    for i in range(len(rain_in_numbers)):
        num_int = []
        for length in range(len(rain_in_numbers[i])):
            num_int.append(int(rain_in_numbers[i][length]))
        numbers.append(num_int)

    return numbers


def day_total(total_numbers):
    totals = []
    for i in total_numbers:
        totals.append(i[0])
    return totals


def mean(total):
    sum = 1
    total_nums = len(total)
    for i in total:
        sum += i

    return sum/total_nums


def most_rain(dates, total):
    max_totals = max(total)
    max_index = total.index(max_totals)
    day = dates[max_index].day
    year = dates[max_index].year
    print(f'Day with most rain: {day}.')
    print(f'Year with most rain: {year}.')


def chart(x,y):
    plt.plot(x,y)
    plt.show()


#v1
rain = comma_sep()
date_time_group = rain_dates(rain)


#v2
numbers = day_total(total_numbers)


