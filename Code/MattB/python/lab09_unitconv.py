"""
This program will convert units of length in between each other.
It takes a user input in one unit and will output the conversion in the desired unit.
"""

# User input
distance = input('Enter a length in feet to convert to meters: ')

convert = float(distance) * 0.3048

print(f'{distance} ft is equal to {convert} m.')