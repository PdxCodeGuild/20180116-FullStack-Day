

print('Welcome to the unit converter!')
print()

# allow user to input units in feet, miles, meters, or kilometers

distance = int(input('What is the distance? '))
input_unit = input('What is the input unit? (ft, mi, m, yd, in, or km) ')
output_unit = input('What is the output unit? (ft, mi, m, yd, in, or km) ')

# creat dictionary with the key as a string and number as a value

convert_from_meters = {'ft': .3048, 'mi': 1609.34, 'm': 1, 'yd': .9144, 'in': 39.370, 'km': .0001}
convert_to_meters = {'ft': 3.28, 'mi': .0006, 'm': 1, 'yd': 1.0936, 'in': .02541, 'km': 1000}

# distance times convert_to lookup input unit

x = distance * convert_to_meters[input_unit]

# save that

print(str(distance) + input_unit + ' is equal to ' + str(x * convert_from_meters[output_unit]) + output_unit)

# meters value convert_from[] lookup output unit



