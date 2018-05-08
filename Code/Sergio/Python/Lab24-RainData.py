"""
Lab 24: Rain Data - Mt. Tabor
"""
import datetime

# defines global string
opendata = 'mttabor.txt'
# list of tuples,
tuples_list = []
days = []
with open(opendata) as f:
    contents = f.read().split('\n')  # new line

for i in range(12, len(contents)):  # skips first 12 lines
    line = contents[i].split()

    if len(line) == 0:
        continue
    date_string = line[0]
    # datetime object
    date = datetime.datetime.strptime(date_string, '%d-%b-%Y')
    if line[1] == '-':
        continue
    daily_total_string = int(line[1])
    tuples_list.append((date, daily_total_string))

# print(tuples_list)


# get average rainfall

total = 0
n = 0
for i in range(len(tuples_list)):
    total += tuples_list[i][1]
    n += 1

print(f'Total rain: {total}')

average = total / n
average_rain = round((total / n) / 100, 2)

print(f'Average daily rainfall in inches: {average_rain}')

# Work out the Mean (the simple average of the numbers) Then for each number: subtract the Mean and square the result (the squared difference).
difference = 0
total_num = 0
for i in range(len(tuples_list)):
    difference = tuples_list[i][1] - average  # subtract mean/average
    squared = difference ** 2  # square ** the result
    total_num += squared
var = total_num / n
variance = round((var / 100), 2)
print(f'Variance is: {variance}')
