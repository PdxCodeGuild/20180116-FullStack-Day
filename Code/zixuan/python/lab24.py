import datetime

class tuple:

    def __init__(self, date, rain):
        self.year = date.year
        self.rain = rain


def load_file():
    tuples = []
    with open('datetime', 'r') as file:
     lines = file.read().split('\n')

    for x in lines:
        date = datetime.datetime.strptime(x.split()[0], '%d-%b-%Y')
        rain = int(x.split()[1])
        tuples.append(tuple(date, rain))
    return tuples

    # load the data
    # return a list of tuples
    # each row of the data will be a tuple containing the date and the daily total



#Find the day which had the most rain.
#Find the year which had the most rain on average.

static_list = load_file()
year_rain = {}
for x in static_list:
    if x.year in year_rain:
        year_rain[x.year] = year_rain[x.year] + x.rain
    else:
        year_rain[x.year] = x.rain




print(year_rain)

max_year = 0
max_year_rain = 0


for date in year_rain:
  if year_rain[date] > max_year_rain:
     max_year = date
     max_year_rain = year_rain[date]

print("the max rain year is "+ str(max_year)+" it has rained "+str(max_year_rain)+" per year")
