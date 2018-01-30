"""
Lab 24
But it never rains in Portland...
"""

import requests
import datetime
import re

r = requests.get('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain')    # because text files are for chumps
data = r.text.split('\n')       # listify

for i in range(0, 11):          # removing comments in the beginning
    data.remove(data[0])
data.pop()                      # removing last blank line

split_data = []
for i in range(len(data)):
    split_data.append(re.split('\s+', data[i]))

print(split_data)

for i in range(len(split_data)):
    date = datetime.datetime.strptime(split_data[i][0], '%d-%b-%Y')
    print(date.year)
    print(date.month)
    print(date.day)
