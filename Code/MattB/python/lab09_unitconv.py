"""
This program will convert units of length in between each other.
It takes a user input in one unit and will output the conversion in the desired unit.
"""

# User input distance
distance = float(input('Enter a distance you wish to convert: '))

# User input for unit of distance
unit = input('Enter the unit of your distance: ')

# User input for desired unit of output
c_unit = input('Enter the unit you wish to convert to: ')

# Makes sure unit inputted and conversion unit are different
if unit == c_unit:
    c_unit = input('Please enter a different unit to convert')

# Meters conversion
elif unit == 'm' and c_unit == 'ft':
    convert = distance / 0.3048
elif unit == 'm' and c_unit == 'km':
    convert = distance / 1000
elif unit == 'm' and c_unit == 'mi':
    convert = distance * 0.0006214

# Kilometer conversion
elif unit == 'km' and c_unit == 'm':
    convert = distance * 1000
elif unit == 'km' and c_unit == 'ft':
    convert = distance * 3280.84
elif unit == 'km' and c_unit == 'mi':
    convert = distance * .6214

# Mile conversion
elif unit == 'mi' and c_unit == 'm':
    convert = distance / .0006214
elif unit == 'mi' and c_unit == 'ft':
    convert = distance * 5280
elif unit == 'mi' and c_unit == 'km':
    convert = distance / .6214

# Feet conversion
elif unit == 'ft' and c_unit == 'm':
    convert = distance / .3048
elif unit == 'ft' and c_unit == 'mi':
    convert = distance / 5280
elif unit == 'ft' and c_unit == 'km':
    convert = distance / 3280.84

# Output converted unit
print(f'{distance} {unit} is equal to {convert} {c_unit}.')
