"""
Allow the user to also enter the units. Then depending on the units, convert the distance into meters.
The units we'll allow are feet, miles, meters, and kilometers.
"""

#get the user imput
Metrics = ['ft', 'mi', 'm', 'km']



distanceInput = float(input('what is the distance that you would like converted?: '))
metricInput = input('what is the metric that you are starting with (ft, mi, m, or km)?: ')

#converting to meters: 1 ft is 0.3048 m, 1 mi is 1609.34 m, 1 m is 1 m, 1 km is 1000 m

if metricInput == Metrics[0]:
    distanceMeters = distanceInput * 0.3048
elif metricInput == Metrics[1]:
    distanceMeters = distanceInput * 1609.34
elif metricInput == Metrics[2]:
    distanceMeters = distanceInput * 1.0
elif metricInput == Metrics[3]:
    distanceMeters = distanceInput * 1000
else:
    print('error please try again ')

print(f'{distanceInput}{metricInput} is {distanceMeters} meters')
