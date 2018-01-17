units = input('what units will you like to use? \n')
x = float(input('conversion amount \n'))

ft = x * 0.3048
miles = x * 1609.34
meters = x * 1
km = x * 1000
yard = x * 0.9144
inch = x * 0.0254

if ft:
    print(ft)

elif meters:
    print(meters)

elif km:
    print(km)

elif yard:
    print(yard)

elif inch:
    print(inch)


