


conversion_table = ['ft', 'mi', 'm', 'km']

distance_input = float(input('what is the distance you would like converted?: '))
conversion_input = input('what is the system that you are starting with (ft, mi, m, or km)?: ')
conversion_output = input('what is the system that you would like the distance converted to (ft, mi, m, or km)?: ')

if conversion_output == conversion_table[0]:
    distance = distance_input * 0.3048
elif conversion_output == conversion_table[1]:
    distance = distance_input * 1609.34
elif conversion_output == conversion_table[2]:
    distance = distance_input * 1.0
elif conversion_output == conversion_table[3]:
    distance = distance_input * 1000
else:
    print('error')


if conversion_output == conversion_table[0]:
    distance = distance_input * 3.28084
elif conversion_output == conversion_table[1]:
    distance = distance_input * 0.000621371
elif conversion_output == conversion_table[2]:
    distance = distance_input * 1
elif conversion_output == conversion_table[3]:
    distance = distance_input * 0.001

else:
    print('error')


print(f'{distance_input}{conversion_input} is {distance}{conversion_output}')