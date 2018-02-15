"""
Lab 24: Rain Data v1
"""
import datetime
import re

# defines global string
opendata = 'mttabor.txt'

# daily rain list
days = []
data = []

with open(opendata) as file:  # opens 'opendata' where mttabor is assigned to
    lines = file.read().split('\n')

for i in range(0, 12):  # skips to line 12
    lines.remove(lines[0])
lines.pop()

# regular expressions
for i in range(len(lines)):
    data.append(re.split('\s+', lines[i]))

# dates
for i in range(len(data)):
    date = datetime.datetime.strptime(data[i][0], '%d-%b-%Y')
    days.append(f"{date.month}/{date.day}/{date.year}")

# print(date.year)
# print(date.month)
# print(date.day)
# print(date.strftime('%d-%b-%Y'))
# print(data)
# print(days)
# print(lines)

# stuck on v2
