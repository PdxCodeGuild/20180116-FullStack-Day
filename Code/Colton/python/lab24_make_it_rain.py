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

print(data)
# print(dates)

# Way to use functions in here? Need to use those more


#########VERSION 2###########
#Decipher the Hieroglyphics
# need to find which day had most rain
# # find which year had the most rainfall on AVERAGE
rainy_day = []
for i in range(len(data[i])):



print(rainy_day)






