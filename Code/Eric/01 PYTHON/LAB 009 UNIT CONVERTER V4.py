#UNIT CONVERTER V4: CONVERSIONS FOR EVERYBODY!!!
unit_dict = {'meters':1, 'feet':0.3048, 'miles':1609.34, 'kilometers':1000, 'yards':0.9144, 'inches':0.0254}

#CONVERT FROM?
unit_type_in = input('\nWhat UNIT of distance would you like to convert?\nTypes:\nMeters?\nFeet?\nMiles?\nKilometers?\nYards?\nInches?\n\n:')

while unit_type_in not in unit_dict.keys():
	unit_type_in = input('\nWhat UNIT of distance would you like to convert?\nTypes:\nMeters?\nFeet?\nMiles?\nKilometers?\nYards?\nInches?\n\n:')

#AMT OF UNITS TO CONVERT?
distance_in = float(input('\nHOW MANY units of distance would you like to convert?\n\n:'))

if distance_in is not float(distance_in):
	print('Please use an integer\n')
	distance_in = float(input('\nHOW MANY units of distance would you like to convert?\n\n:'))

#CONVERT TO?
unit_type_out = input('\nWHAT UNIT of distance would you like to convert TO?\nTypes:\nMeters?\nFeet?\nMiles?\nKilometers?\nYards?\nInches?\n\n:')

while unit_type_out not in unit_dict.keys():
	unit_type_out = input('\nWHAT UNIT of distance would you like to convert TO?\nTypes:\nMeters?\nFeet?\nMiles?\nKilometers?\nYards?\nInches?\n\n:')

#QUICK MATHS
conversion_out = (float(distance_in) * (unit_dict[unit_type_in]))
print('\nIt looks like ' + str(distance_in) + ' ' + unit_type_in + ' is equivalent to ' + str(conversion_out / unit_dict[unit_type_out]) + ' ' + unit_type_out + '!')