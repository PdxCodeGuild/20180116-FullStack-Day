#Make a dictionary for unit values

unit_dictionary = {'meter': 1.0, 'foot': 0.3048,  'feet': 0.3048, 'mile': 1609.34, 'kilometer': 1000, 'm': 1.0, 'ft': 0.3048, 'mi': 1609.34, 'km': 1000 }

# Define the units to be input and output
input_unit = input("What unit of measurement would you like to convert from?\n:")
input_scale = unit_dictionary[input_unit]

output_unit = input("What unit of measurement would you like to convert to?\n:")
output_scale = unit_dictionary[output_unit]

distance = float(input("What is the distance? \n:"))

input_to_meter = (distance * input_scale)
output_to_meter = (distance * output_scale)

output_to_distance = (input_to_meter // output_to_meter)


print(f'{distance} {input_unit} = {output_to_distance} {output_unit}')




#output_unit = unit_dictionary[input("What unit of measurement would you like to convert to?\n:")]

# Define how many to convert

"""
number_of_units = int(input("How many units would you like to convert?\n:"))

# Calculate units to maths

input_number = unit_dictionary['input_unit']
output_number = unit_dictionary['output_unit']


# Calculate conversion

total_units = int("")

if input_unit > 1:
    total_units = total_units + (input_unit * output_unit)
elif input_unit < 1:
    total_units = total_units + (input_unit // output_unit)


# Print

print("There are " + str(total_units)  + " " + str(output_unit) + " in " + str(input_unit) +  ".")

"""