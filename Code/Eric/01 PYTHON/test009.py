unit_dict = {'meters':1, 'feet':0.3048, 'miles':1609.34, 'kilometers':1000, 'yards':0.9144, 'inches':0.0254}

unit_type_in = input("\nWhat UNIT of distance would you like to convert? Type:\nMeters?\nFeet?\nMiles?\nKilometers?\nYards?\nInches?\n\n:")

while unit_type_in not in unit_dict.keys():
    unit_type_in = input("\nWhat UNIT of distance would you like to convert? Type:\nMeters?\nFeet?\nMiles?\nKilometers?\nYards?\nInches?\n\n:")

distance_in = input("\nHOW MANY units of distance would you like to convert?\n\n:")

while True:
    try:
        float(distance_in)
        break
    except:
        print("Please use an integer\n")
        distance_in = input("HOW MANY units of distance would you like to convert?\n\n:")

unit_type_out = input("\nWHAT UNIT of distance would you like to convert TO? Type:\nMeters?\nFeet?\nMiles?\nKilometers?\nYards?\nInches?\n\n:")

while unit_type_out not in unit_dict.keys():
    unit_type_out = input("\nWHAT UNIT of distance would you like to convert TO? Type:\nMeters?\nFeet?\nMiles?\nKilometers?\nYards?\nInches?\n\n:")

conversion_out = (float(distance_in) * (unit_dict[unit_type_in]))

print("\nIt looks like " + str(distance_in) + " " + unit_type_in + " is equivalent to " + str(conversion_out / unit_dict[unit_type_out]) + " " + unit_type_out + "!")
