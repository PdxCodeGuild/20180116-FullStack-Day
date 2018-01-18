#v2
user = input("What unit would you like to convert?\n:")
user2 = input('What would you like to convert to?\n:')
number_dist = int(input('Distance?\n:'))
meter_to = {'feet':3.2808399, 'meter':1, 'kilometers':1000, 'mile':0.00062137}
feet_to = {'meter':0.3048, 'mile':0.00018939, 'kilometer':0.0003047, 'feet':1}
kilometer_to = {'meter':0.001, 'kilometer':1, 'mile':1.609344, 'feet':0.0003047}
mile_to = {'kilometer':1.609344, 'meter':1609.344, 'feet':5280, 'mile':1}

#meter
if user == 'meter' and user2 == 'feet':
    print(number_dist * meter_to['feet'])
if user == 'meter' and user2 == 'kilometers':
    print(number_dist / meter_to['kilometers'])
if user == 'meter' and user2 == 'mile':
    print(number_dist * meter_to['mile'])
#feet
if user == 'feet' and user2 == 'meter':
    print(number_dist * feet_to['meter'])
if user == 'feet' and user2 == 'mile':
    print(number_dist * feet_to['mile'])
if user == 'feet' and user2 == 'kilometer':
    print(number_dist * feet_to['kilometer'])
#kilometer
if user == 'kilometer' and user2 == 'feet':
    print(number_dist * kilometer_to['feet'])
if user == 'kilometer' and user2 == 'mile':
    print(number_dist * kilometer_to['mile'])
if user == 'kilometer' and user2 == 'meter':
    print(number_dist * kilometer_to['meter'])
#mile
if user == 'mile' and user2 == 'feet':
    print(number_dist * mile_to['feet'])
if user == 'mile' and user2 == 'kilometer':
    print(number_dist * mile_to['kilometer'])
if user == 'mile' and user2 == 'meter':
    print(number_dist * mile_to[kilometer])

