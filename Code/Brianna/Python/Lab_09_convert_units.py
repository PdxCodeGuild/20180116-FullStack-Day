
# Get ready to convert values
def convert_units(distance, input_unit, output_unit):
    units = {'meter': 1.0, 'foot': 0.3048,  'feet': 0.3048, 'mile': 1609.34, 'kilometer': 1000, 'm': 1.0, 'ft': 0.3048, 'mi': 1609.34, 'km': 1000 }
    return distance * units[input_unit] / units[output_unit]

# Define the units to be input and output
input_unit = input("What unit of measurement would you like to convert from?\n:")
output_unit = input("What unit of measurement would you like to convert to?\n:")

# Get the distance we are converting
distance = float(input("What is the distance? \n:"))

# Call convert_units function to find the answer.
answer = convert_units(distance, input_unit, output_unit)

print(f' {str(distance)} {str(input_unit)}s in {str(output_unit)}s is {str(answer)}.')

