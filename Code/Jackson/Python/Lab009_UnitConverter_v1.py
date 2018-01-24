"""
Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can
get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
"""


distance_feet = int(input('what is the distance in feet? '))
distance_meters = distance_feet * 0.3048

print(f'{distance_feet} ft is {distance_meters} meters')



