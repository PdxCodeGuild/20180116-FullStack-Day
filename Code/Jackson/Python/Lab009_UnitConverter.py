"""
This lab will involve writing a program that allows the user to convert a number between units.
**Still need to convert version 3 - yards and inches.

"""

#get the user imput

Metrics = ['ft', 'mi', 'm', 'km']

#units_ft = 'ft'
#scales = [0.3048, 1609.34, ...]



distanceInput = float(input('what is the distance that you would like converted?: '))
metricInput = input('what is the metric that you are starting with (ft, mi, m, or km)?: ')
metricOutput = input('what is the metric that you would like the distance converted to (ft, mi, m, or km)?: ')
distanceOutput = 0.0
distanceMeters = 0.0

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

#all the same metrics
if metricInput == Metrics[0] and metricOutput == Metrics[0]:
    distanceOutput = distanceInput * 1

if metricInput == Metrics[1] and metricOutput == Metrics[1]:
    distanceOutput = distanceInput * 1

if metricInput == Metrics[2] and metricOutput == Metrics[2]:
    distanceOutput = distanceInput * 1

if metricInput == Metrics[3] and metricOutput == Metrics[3]:
    distanceOutput = distanceInput * 1

#output meters
if metricOutput == Metrics[2]:
    distanceOutput = distanceMeters

#output ft
if metricOutput == Metrics[0] and metricOutput != Metrics[2]:
    distanceOutput = distanceInput / 0.3048

#output mi
if metricOutput == Metrics[1] and metricOutput != Metrics[2]:
    distanceOutput = distanceInput / 1609.34

#output km
if metricOutput == Metrics[3] and metricOutput != Metrics[2]:
    distanceOutput = distanceInput / 1000

#print out answer
print(str(distanceInput) + str(metricOutput) + ' is equal to ' + str(distanceOutput) + str(metricOutput))




