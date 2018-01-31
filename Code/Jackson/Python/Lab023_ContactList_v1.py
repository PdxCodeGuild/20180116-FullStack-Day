"""
Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together,
and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert
the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys,
the text in the other lines represent the values.
"""


with open('contacts_csv.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

#hardcode the key names from the header
username = 'name'
favfruit = 'favorite fruit'
favcolor = 'favorite color'

contacts = []
# create lists for each data point in line and use to create dictionary
for i in range(1, len(lines)):
    cells = lines[i].split(',')
    #print(cells) #test
    dictionary = {username:cells[0], favfruit:cells[1], favcolor:cells[2]}
    contacts.append(dictionary) #add dictionary to the list

print(contacts)

#print(contacts[0]['favorite fruit']) #this is how you access Maggie's favorite fruit