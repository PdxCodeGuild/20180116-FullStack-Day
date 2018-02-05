import re
from datetime import datetime

# open .txt file and splits the file at the line breaks and assigns it to the variable contents, this portion works
with open('raindata_scratch.txt', 'r') as file:
    contents = file.read().split('\n')
    # print(contents)


data_l = []

for i in range(len(contents)):
    data_l.append(re.split('\s+', contents[i]))
    # print(contents)

date_l = []

for dates in range(len(data_l)):
    if len(data_l[dates][0]) > 11:
        date_l.append(datetime.strptime(data_l[dates][0], '%d/%b/%y'))

print(data_l)

for i in range(len(date_l)):
    print(date_l[i].year, date_l[i].month, date_l[i].day)

