'Unit converter for meters'

from time import sleep
# get number of feet
#print out equivalence in meters.

ft_m = 0.3048 #feet in meters
mi_m = 1609.34 #mile in meters
km_m = 1000 #km in meters

def main():
    print('Unit Conversion Calculator for meters\n\nStep 1: Enter the distance')
    distance = input('Distance:  ')
    print('Now choose the units for the distance entered.\n(input ft, mi, or km)')
    units = input('Units: ')


    if units == 'ft':
        print(distance, units, 'equals', int(distance) * ft_m, ' meters')
    if units == 'mi':
        print(distance, units, 'equals', int(distance) * mi_m, ' meters')
    elif units == 'km':
        print(distance, units, 'equals', int(distance) * km_m, ' meters')
    sleep(2)

    print('\nThanks for using this unit converter.\nGoodbye!\n')