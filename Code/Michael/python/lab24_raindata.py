import re
from datetime import datetime

# open .txt file and splits the file at the line breaks and assigns it to the variable contents, this portion works
with open('raindata_scratch.txt', 'r') as file:
    contents = file.read().split('\n')
    # print(contents)


# to strip off the header data so the file can be properly parsed.
for i in range(0, 12):
    contents.remove(contents[0])
contents.pop()


# iterate over contents with range and len and each indices the white space is removed with the regular expression with a plus indicating to remove the white space of one or more instance and append it to data_list list
data_l = []
for i in range(len(contents)):
    data_l.append(re.split('\s+', contents[i]))
    # print(contents)


# interate over the list data_l with range and len and pass them to dates and if len is greater than 11 we append its output to date_l and with striptime, we convert the dates into its new format
date_l = []
for dates in range(len(data_l)):
    if len(data_l[dates][0]) > 11:
        date_l.append(datetime.strptime(data_l[dates][0], '%d/%b/%y'))


sum_l = []
for i in range(len(data_l)):
    try:
        sum_l.append(int(data_l[i][1]))
    except ValueError:
        sum_l.append(0)


total = len(sum_l)
sums = 0
for i in range(len(sum_l)):
    sums += sum_l[i]


def mean(total, sums):
    mean = (1 / total) * sums
    return mean


def vari(mean):
    variance = 0
    for i in range(len(sum_l)):
        variance += (sum_l[i] - mean) ** 2
    var = (1 / total) * variance
    return var


mean = mean(total, sums)
variance = vari(mean)

print(f'The mean is: {round(mean, 2)}')
print(f'The variance is: {round(variance, 2)}')