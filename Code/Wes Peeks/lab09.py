# v4


def standardize_units(units):
    units = units.lower()
    if units in ['m', 'meter', 'meters']:
        units = 'meter'
    return units


unit1 = input("What unit would you like to convert?\n:")
unit2 = input('What would you like to convert to?\n:')

unit1 = standardize_units(unit1)
unit2 = standardize_units(unit2)


number_dist = int(input('Distance?\n:'))
meter_to = {'feet': 3.2808399, 'meter': 1, 'kilometers': 1000, 'mile': 0.00062137}
feet_to = {'meter': 0.3048, 'mile': 0.00018939, 'kilometer': 0.0003047, 'feet': 1}
kilometer_to = {'meter': 0.001, 'kilometer': 1, 'mile': 1.609344, 'feet': 0.0003047}
mile_to = {'kilometer': 1.609344, 'meter': 1609.344, 'feet': 5280, 'mile': 1}

# meter
if unit1 == 'meter' and unit2 == 'feet':
    print(number_dist * meter_to['feet'])
if unit1 == 'meter' and unit2 == 'kilometers':
    print(number_dist / meter_to['kilometers'])
if unit1 == 'meter' and unit2 == 'mile':
    print(number_dist * meter_to['mile'])
# feet
if unit1 == 'feet' and unit2 == 'meter':
    print(number_dist * feet_to['meter'])
if unit1 == 'feet' and unit2 == 'mile':
    print(number_dist * feet_to['mile'])
if unit1 == 'feet' and unit2 == 'kilometer':
    print(number_dist * feet_to['kilometer'])
# kilometer
if unit1 == 'kilometer' and unit2 == 'feet':
    print(number_dist * kilometer_to['feet'])
if unit1 == 'kilometer' and unit2 == 'mile':
    print(number_dist * kilometer_to['mile'])
if unit1 == 'kilometer' and unit2 == 'meter':
    print(number_dist / kilometer_to['meter'])
# mile
if unit1 == 'mile' and unit2 == 'feet':
    print(number_dist * mile_to['feet'])
if unit1 == 'mile' and unit2 == 'kilometer':
    print(number_dist * mile_to['kilometer'])
if unit1 == 'mile' and unit2 == 'meter':
    print(number_dist * mile_to['kilometer'])
