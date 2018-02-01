"""
Download one of these files (or the csv I've compiled containing all of them), and write a function to load the file.
Each line of the file will become a list or class or tuple consisting of a datetime and a series of ints.

"""
import datetime

#load the file
# nameoffile = input('what is the name of the file that you would like the ARI computed for (add .txt): ')
file = 'RainyDay.txt'

with open(file) as f:  # open the file. file was downloaded and added to repository
    contents = f.read().split('\n')  # splits every new line
    #contents = f.read()  # list of all the lines as strings (not sentences)


daily_totals = []
for i in range(12,len(contents)):
    line = contents[i].split() # line is a list of strings, because split() with no parameters splits on spaces/tabs
    #print(line)
    # data_name = contents[i][:11]
    # data_name = []
    if len(line) == 0:
        continue
    date_str = line[0] # date and time are at index 0
    date = datetime.datetime.strptime(date_str, '%d-%b-%Y') #convert to a 'datetime' data type
    if line[1] == '-':
        continue
    daily_total_str = int(line[1])
    daily_total_tuple = (date, daily_total_str)

    # use a 'continue' on loop when converting data to ints (missing days won't convert)


    daily_totals.append(daily_total_tuple) #append the tuple in the line above to the list
    # print(date_str)
    # print(daily_total_str)
    # print()


print(daily_totals)



