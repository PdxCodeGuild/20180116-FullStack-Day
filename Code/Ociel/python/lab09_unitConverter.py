# Version 1

feet = input("what is the distance in feet? ")
feet_to_meter = float(feet) * 0.3048
print(f"{feet} ft is {round(feet_to_meter,4)} m \n\n\n")


#
# # Version 2 and 3
#
# userInput = float(input("What is the distance: "))
# unit = input("What is the unit (Ex: ft, mi, m, km, yard, inch ")
#
# myDic = {'ft': 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000, 'yard': 0.9144, 'inch': 0.0254}
# print(f'{userInput} mi is {userInput * myDic[unit]} m')


# # Version 4
# userInputs = float(input("What is the distance: "))
# input_units = input("What is the input units (Ex: ft, mi, m, km, yard, inch) ")
# output_units = input("what are the output units? ")
#
# myDict = {'ft': 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000, 'yard': 0.9144, 'inch': 0.0254}
# firstConversion =  myDict[input_units] / myDict['m']
#
#
# print(f'{userInputs} {input_units} is {round((firstConversion / myDict[output_units]) * 100, 7)} {output_units}\n\n')
#

