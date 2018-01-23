print("""
1. feet to meters
2. miles to meters
3. kilometers to meters
4. yards to meters
5. inches to meters
""")

units = input('Select a conversion type. \n> ')

x = float(input('what is the distance? \n> '))

if units == '1':
    print(x * 0.3048,'meters')

elif units == '2':
    print(x * 1609.34,'meters')

elif units == '3':
    print(x * 1000,'meters')

elif units == '4':
    print(x * 0.9144,'meters')

elif units == '5':
    print(x * 0.0254,'meters')

else:
    print('The metric system is the tool of the Devil!')


