"""
Now we'll ask the user for the distance, the starting units, and the units to convert to.
You can think of the values for the conversions as elements in a matrix, where the rows will be the units
you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values
will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).
"""

#get the user imput
Metrics = ['ft', 'mi', 'm', 'km']

distanceInput = float(input('what is the distance that you would like converted?: '))
metricInput = input('what is the metric that you are starting with (ft, mi, m, or km)?: ')
metricOutput = input('what is the metric that you would like the distance converted to (ft, mi, m, or km)?: ')

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



if metricOutput == Metrics[0]:
    distanceOutput = distanceMeters * 3.28084
elif metricOutput == Metrics[1]:
    distanceOutput = distanceMeters * 0.000621371
elif metricOutput == Metrics[2]:
    distanceOutput = distanceMeters * 1
elif metricOutput == Metrics[3]:
    distanceOutput = distanceMeters * 0.001

else:
    print('error please try again ')


print(f'{distanceInput}{metricInput} is {distanceOutput} {metricOutput}')