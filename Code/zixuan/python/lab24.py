import datetime
date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')




with open('datetime', 'r') as file:
    lines = file.read().split('\n')


max = 0
max_date = ""

for x in lines:
    x = x.split()
    if max < int(x[1]):
        max = int(x[1])
        max_date = x[0]

print(max_date)