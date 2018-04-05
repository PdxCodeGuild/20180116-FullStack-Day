


conversion_table = ['ft', 'mi', 'm', 'km']

distance_input = float(input('what is the distance you would like converted?: '))
units_input = input('what is the system that you are starting with (ft, mi, m, or km)?: ')
units_output = input('what is the system that you would like the distance converted to (ft, mi, m, or km)?: ')

if units_input == conversion_table[0]:
    distance = distance_input * 0.3048
elif units_input == conversion_table[1]:
    distance = distance_input * 1609.34
elif units_input == conversion_table[2]:
    distance = distance_input * 1.0
elif units_input == conversion_table[3]:
    distance = distance_input * 1000
else:
    print('error')


if units_output == conversion_table[0]:
    distance = distance / 0.3048
elif units_output == conversion_table[1]:
    distance = distance / 1609.34
elif units_output == conversion_table[2]:
    distance = distance * 1
elif units_output == conversion_table[3]:
    distance = distance * 0.001
else:
    print('error')


print(f'{distance_input}{units_input} is {distance}{units_output}')