"""
Add support for yards, and inches.
1 yard is 0.9144 m
1 inch is 0.0254 m
"""

#get the user imput
Metrics = ['ft', 'mi', 'm', 'km', 'yd', 'in']

distanceInput = float(input('what is the distance that you would like converted?: '))
metricInput = input('what is the metric that you are starting with (ft, mi, m, km, yd, or in)?: ')

#converting to meters: 1 ft is 0.3048 m, 1 mi is 1609.34 m, 1 m is 1 m, 1 km is 1000 m

if metricInput == Metrics[0]:
    distanceMeters = distanceInput * 0.3048
elif metricInput == Metrics[1]:
    distanceMeters = distanceInput * 1609.34
elif metricInput == Metrics[2]:
    distanceMeters = distanceInput * 1.0
elif metricInput == Metrics[3]:
    distanceMeters = distanceInput * 1000
elif metricInput == Metrics[4]:
    distanceMeters = distanceInput * 0.9144
elif metricInput == Metrics[5]:
    distanceMeters = distanceInput * 0.0254
else:
    print('error please try again ')

print(f'{distanceInput} {metricInput} is {distanceMeters} meters')