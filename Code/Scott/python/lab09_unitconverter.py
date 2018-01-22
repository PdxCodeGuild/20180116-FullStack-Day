

print('Welcome to the unit converter!')
print()

# allow user to input units in feet, miles, meters, or kilometers

distance = int(input('What is the distance? '))
unit_measure = input('What is the input unit? (ft, mi, m, yd, in, or km)? ')


if unit_measure == 'ft':
    meters = distance * .3048
    print(str(distance) + ' ft is equal to ' + str(meters) + ' m')
elif unit_measure == 'mi':
    meters = distance * 1609.34
    print(str(distance) + ' miles is equal to ' + str(meters) + ' m')
elif unit_measure == 'm':
    meters = distance * 1
    print(str(distance) + ' meters is equal to ' + str(meters) + ' m')
elif unit_measure == 'km':
    meters = distance * 1000
    print(str(distance) + ' kilometers is equal to ' + str(meters) + ' m')
elif unit_measure == 'yd':
    meters = distance * .9144
    print(str(distance) + ' yards is equal to ' + str(meters) + ' m')
elif unit_measure == 'in':
    meters = distance * .0254
    print(str(distance) + ' in is equal to ' + str(meters) + ' m')
else:
    print('You entered an invalid unit of measure.')



