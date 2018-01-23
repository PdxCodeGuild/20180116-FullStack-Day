# Unit converter for meters


def to_meters(dist, units):
    if units == 'ft':
        return dist * 0.3048  # feet in meters
    elif units == 'mi':
        return dist * 1609.34  # mile in meters
    elif units == 'km':
        return dist * 1000  # etc.
    elif units == 'yd':
        return dist * 0.9144
    elif units == 'in':
        return dist * 0.0254
    elif units == 'm':
        return dist


def from_meters(dist, units):
    if units == 'm':
        return dist  # no conversion needed
    elif units == 'ft':
        return dist / 0.3048
    elif units == 'mi':
        return dist / 1609.34
    elif units == 'km':
        return dist / 1000
    elif units == 'yd':
        return dist / 0.9144
    elif units == 'in':
        return dist / 0.0254


def main():
    print('Unit Conversion Calculator\n\nStep 1: Enter the distance')
    distance = float(input('Distance:  '))
    print('Units for this distance.\n(input ft, mi, km, yd, or in)')
    units = input('Units: ')
    units_to = input('what units will this be converted to? ')

    d_in_meters = to_meters(distance, units)
    dist_to = from_meters(d_in_meters, units_to)
    output = f'{distance} {units} is {dist_to} {units_to}'
    print(output)


main()
print('\nThanks for using this unit converter.\nGoodbye!\n')
