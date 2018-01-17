"""
Lab 9
Let's convert some units!
"""

print("Welcome to the unit converter! The acceptable units are in, ft, yd, mi, cm, m, and km.\n")

cont = 'y'

while cont == 'y':
    while True:
        number = input("Enter your length: ")
        try:
            number = float(number)
            break
        except ValueError:
            print("Please enter a number.")

    input_unit = input("Enter the original unit: ")
    output_unit = input("Enter the unit you would like to convert to: ")

    meter_conversion_dict = {'in': 39.37008, 'ft': 3.28084, 'yd': 1.09361, 'mi': 0.000621371, 'cm': 100, 'm': 1, 'km': 0.001}
    def convert_units(number, input_unit, output_unit):
        meters = number / meter_conversion_dict[input_unit]
        return meters * meter_conversion_dict[output_unit]

    result = convert_units(number, input_unit, output_unit)
    print(f"{number} {input_unit} is {result} {output_unit}\n")

    cont = input("Would you like to convert another unit? y/n: ")

print("Thanks for using the unit converter. Have a nice day!\n")
