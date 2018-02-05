import datetime
import re #regular expressions module Need to read more into these



with open('hayden_island.csv') as file:
    lines = file.read().split('\n') # is there a way to import directly from site? Possible idea for capstone

for i in range(0, 12): # removing last line, otherwise the dates won't format
    lines.remove(lines[0])
lines.pop()

data = [] # data with dates
for i in range(len(lines)):
    data.append(re.split('\s+', lines[i])) #s+ matches blank spaces from regular expressions


dates = [] #just the dates
for i in range(len(data)):
    date = datetime.datetime.strptime(data[i][0], '%d-%b-%Y')
    dates.append(f"{date.month}/{date.day}/{date.year}")

#print(data)
# print(dates)

# Way to use functions in here? Need to use those more


#########VERSION 2###########
#Decipher the Hieroglyphics
# need to find which day had most rain
# # find which year had the most rainfall on AVERAGE

###pull the daily total####
daily_total = [] #puling all of the rain totals for each day?
for i in range(len(data)):
    daily_total.append(data[i][1:2])
daily_total = [day for dates in daily_total for day in dates]


most_rain = max(daily_total) #finds the biggest number

location = daily_total.index(max(daily_total)) # finds the day with the most rain

rainiest_day = (dates[location]) #both date and daily total are the same length so the rain and dates are at the same indices

print(f''' The wetest date was {rainiest_day} with {most_rain} inches of rain.''')

###Pull the rainiest year on average###


















