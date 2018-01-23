def get_distance():
    #Ask user for original distance in float value
    while True:
        a = input('Please enter a distance...')
        try:
            a = float(a)
            break
        except ValueError:
            print('please enter a number')
    return a

def get_in_units():
    #ask user for units of input distance
    print('These are valid units: ', units)
    u = input ('What are you converting from? ')
    while u not in units:
        u = input('Enter a valid unit please.')
    return u


def get_out_units():
    # ask user for desired output units
    print('These are valid units: ', units)
    u = input('What are you converting to? ')
    while u not in units:
        u = input('Enter a valid unit please.')
    return u

#List Variables containing conversion factors and valid units

to_m_factors = [.3048, .9144, .0254, 1609.344, 1.0, 1000.0]
from_m_factors = [1/.3048, 1/.9144, 1/.0254, 1/1609.344, 1.0, 1/1000.0]
units = ['ft', 'y', 'in', 'mi', 'm', 'km']


distance = get_distance() #Get distance from user
in_units = get_in_units() #Get the input units
out_units = get_out_units() #Get the output units
to_m_factor = to_m_factors[units.index(in_units)] #Choose conversion factor to meters
from_m_factor = from_m_factors[units.index(out_units)] #Choose conversion factor from meters
meters = round(distance * to_m_factor, 4) # Compute meters
final = round(meters * from_m_factor, 4)  #Compute distance in output units
print (distance, in_units, " is ", final, out_units)

